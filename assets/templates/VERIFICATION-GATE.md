# Mandatory remote browser verification gate

No remote-control feature, fix, refactor, dependency update, packaging change, or release is complete until every relevant gate below passes and the handoff reports evidence.

## Product ceilings

Fill these before implementation:

- cold connection p95:
- trusted reconnect p95:
- idle command acknowledgement p95/p99:
- saturated command acknowledgement p95/p99:
- first snapshot/file publication:
- sustained bulk throughput floor:
- browser/Rust memory and queue ceilings:
- beacon/host recovery ceiling:

## Required sequence

1. Add focused Rust/browser/contract tests for the changed behavior and denial paths.
2. Build fresh optimized Rust and production browser assets inside the gate.
3. Run format, lint, type, unit, integration, schema, capability, and production-build checks defined by the repository.
4. If transfer changed, run digest/offset/failure/incremental-publication/saturation/resource/soak gates.
5. Run the real browser-to-authority scenarios across the supported browser matrix.
6. Run direct, forced-relay, restrictive failure, reconnect, sleep/wake, and network-handoff cases relevant to the transport claim.
7. Exercise the exact packaged/installed host adapter and production CSP/capabilities.
8. Fetch the public static companion and prove authentication, snapshot, one applied action, and promised media/transfer against the installed app.
9. If supervised, kill only the exact host process, prove distinct replacement and fresh discoverability without product activation, test deliberate off, then restore.
10. Record commands, pass counts, versions, route evidence, benchmark/resource artifacts, hashes, and all not-run matrix entries.

Mocks, compilation, screenshots, API health checks, signaling success, or a backend “on” flag never replace the real browser/native result.

## Handoff format

```text
Changed:
Passed:
Measured:
Installed/public evidence:
Not run:
Pre-existing failures:
Residual risk:
```
