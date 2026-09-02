# Remote-control starter

These files provide a transport-neutral boundary for a remote-enabled Rust/Tauri application. Copy them with `scripts/scaffold_remote_control.py`, then replace the example action/state profile with product semantics.

The starter includes:

- JSON application-profile, wire-envelope, remembered-device, and transfer schemas;
- a pure Rust authority with grant checks, revisions, expected-revision handling, and fingerprinted command deduplication;
- strict browser protocol validation and binary-frame framing;
- a Playwright scenario outline for the real browser/native gate.

It intentionally does **not** include:

- a hand-written PAKE or remembered-device cryptography;
- signaling, STUN, TURN, VDO.Ninja credentials, or production endpoints;
- arbitrary Tauri commands, filesystem paths, shell access, or generic remote input;
- a claim that copied code is production-ready.

Integrate a maintained implementation of OPAQUE, SPAKE2+, or SPAKE2 for human-password authentication, bind its authenticated result to the Rust grant API, and qualify the complete installed path.

Run the standalone checks:

```bash
cargo test --manifest-path rust/Cargo.toml
npm --prefix browser test
```
