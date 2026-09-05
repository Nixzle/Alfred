# Event-Driven Presence

Purpose: prefer trustworthy event-triggered observation over polling when a real event surface exists.

## Trigger model

A source event should carry enough metadata to establish:
- source identity;
- event type;
- observed/effective time;
- deduplication or stable event identifier when available;
- project/user/surface scope;
- confidence or verification state when material.

Presence then decides whether to ignore, retain, surface, investigate or prepare action. The event itself never grants authority.

## Requirements

- deduplicate correlated/replayed events;
- bound fan-out and repeated wakeups;
- preserve source provenance;
- treat stale events as historical evidence, not current truth;
- isolate untrusted event payloads from instructions;
- fall back to polling only when the source cannot provide reliable events and the monitoring need justifies it.

## Status

This is canonical doctrine. Mechanical event-driven observation exists only on surfaces with verified event/webhook/runtime support. No event surface means no claim of ambient observation.
