"""Score supplied semantic judgments against explicitly attributed reference labels."""
import argparse
import hashlib
import json
from pathlib import Path

LABELS = ('supported', 'unsupported', 'uncertain')


def digest(dataset):
    return hashlib.sha256(json.dumps(dataset, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def score(dataset, trial):
    """Measures label agreement, not independent truth or general model capability."""
    cases = dataset['cases']
    expected = {c['id']: c for c in cases}
    answers = trial['answers']
    actual = {a['id']: a for a in answers}
    if not cases or len(expected) != len(cases) or len(actual) != len(answers):
        raise ValueError('nonempty unique cases and unique answers required')
    if set(actual) != set(expected) or trial.get('dataset_sha256') != digest(dataset):
        raise ValueError('exact case coverage and dataset digest required')
    for obj in (dataset['label_provenance'], trial['reviewer']):
        if obj.get('method') not in ('human', 'agent', 'deterministic') or not obj.get('name'):
            raise ValueError('explicit reviewer provenance required')
    matrix = {label: {other: 0 for other in LABELS} for label in LABELS}
    disagreements = []
    for key, case in expected.items():
        answer = actual[key]
        gold, predicted = case['label'], answer['verdict']
        if gold not in LABELS or predicted not in LABELS or not answer.get('note'):
            raise ValueError('valid labels and judgment notes required')
        source_ids = {s['id'] for s in case['sources']}
        if not answer.get('sources') or not set(answer['sources']) <= source_ids:
            raise ValueError('judgment must reference supplied evidence')
        matrix[gold][predicted] += 1
        if gold != predicted:
            disagreements.append(dict(id=key, expected=gold, actual=predicted))
    n = len(cases)
    non_supported = sum(c['label'] != 'supported' for c in cases)
    false_support = sum(matrix[label]['supported'] for label in ('unsupported', 'uncertain'))
    return dict(status='SCORED', cases=n, agreement=(n-len(disagreements))/n,
                false_support_count=false_support,
                false_support_rate=false_support/non_supported if non_supported else None,
                uncertain_predictions=sum(matrix[label]['uncertain'] for label in LABELS),
                confusion_matrix=matrix, disagreements=disagreements,
                dataset_sha256=digest(dataset), label_provenance=dataset['label_provenance'],
                reviewer=trial['reviewer'], trial_design=trial.get('design', 'unspecified'),
                scope='Agreement with supplied labels only; provenance is declared, not authenticated. No capability gain inferred.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, required=True)
    parser.add_argument('--trial', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(score(json.loads(args.dataset.read_text(encoding='utf-8')),
                           json.loads(args.trial.read_text(encoding='utf-8'))), indent=2))
