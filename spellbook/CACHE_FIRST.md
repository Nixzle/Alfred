# Cache First

Use before expensive repeated research, reasoning or tool execution when a fresh authoritative prior result may already satisfy the request.

## Procedure
1. Identify the material cache key: objective, project/scope, source/version, runtime profile, freshness horizon and authority context.
2. Check available fresh authoritative state before repeating expensive work.
3. Reuse only when the cached result still satisfies the current acceptance contract.
4. Revalidate when the user requests current/live state, the domain is volatile, the source/version changed, authority changed, or prior evidence was incomplete.
5. Record cache hits/misses where Watcher evidence can materially improve routing efficiency.

## Rule
Cache First reduces redundant work. It must never launder stale evidence into a current claim.
