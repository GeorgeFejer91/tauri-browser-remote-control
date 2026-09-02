# Tauri Browser Remote Control

A production-minded Codex skill for building Rust/Tauri applications whose local authority can be securely controlled by a complementary static browser app on phones and computers.

This repository synthesizes three evidence streams:

- [Browser Remote Sync Protocol](https://github.com/GeorgeFejer91/browser-remote-sync-protocol): transport-neutral command/state semantics, authenticated peer setup, scope negotiation, and browser qualification.
- [Tauri Rust Developer Skill](https://github.com/GeorgeFejer91/tauri-rust-developer-skill): idiomatic Rust/Tauri boundaries, capabilities, sidecars, lifecycle, packaging, performance, and verification.
- [Zuradio](https://github.com/GeorgeFejer91/zuradio): a real static web companion controlling a local Rust music authority through password-gated WebRTC, trusted-browser access, live media, file upload, supervision, and installed/public browser gates.

It does not incorporate unrelated search-workflow or UI-style skills.

## What the skill teaches

- one Rust authority shared by local UI, CLI, Tauri IPC, and remote adapters;
- a closed typed application protocol instead of remote desktop or generic command forwarding;
- reliable control, replaceable state, optional media, and separately backpressured binary transfer lanes;
- PAKE-based human-password authentication and revocable 24-hour browser-device authorization;
- WebRTC/WSS/WebTransport selection with honest direct/relay reachability claims;
- transactional, digest-bound, incrementally published, optionally resumable file transfer;
- Tauri capability isolation, loopback bootstrap protection, browser lifecycle recovery, and supervised host availability;
- measurable latency, throughput, memory, failure, browser, device, packaged-app, and public-site release gates.
- the underlying Tauri app foundation: idiomatic Rust, plugins/capabilities, persistence, sidecars, mobile/desktop lifecycle, migration, packaging, signing, and updates.

## Install

Install the repository as a Codex skill from GitHub, or copy the repository directory into the Codex skills directory. The root [SKILL.md](SKILL.md) is the entry point.

Invoke it as:

```text
$tauri-browser-remote-control
```

Example:

```text
Use $tauri-browser-remote-control to add a static phone companion to this Tauri app. Keep Rust authoritative, use a human password plus revocable 24-hour device trust, and qualify control latency during a 1 GiB upload.
```

## Repository map

```text
SKILL.md                     concise operating workflow and routing
references/                  detailed protocol, security, transport, and test guidance
assets/starter/              reusable Rust/browser contracts and qualification scaffold
assets/templates/            project documents and mandatory gate templates
scripts/scaffold_remote_control.py
scripts/check_repository.py
tests/                       deterministic repository and scaffold tests
```

## Design boundary

This is application-semantic remote control. It intentionally excludes arbitrary keyboard/mouse injection, screen capture, shell access, unrestricted filesystem access, generic Tauri command proxies, and silent background enablement. Those are materially different products and threat models.

The starter code deliberately does not implement a PAKE. Cryptography should come from a reviewed implementation of a standardized protocol, selected for the project's platform and maintenance constraints. The supplied contracts make the boundary around that implementation explicit.

## Validate

```bash
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
cargo test --manifest-path assets/starter/rust/Cargo.toml
npm --prefix assets/starter/browser test
```

See [references/10-qualification.md](references/10-qualification.md) for application-level gates; repository tests alone do not qualify a generated application.

## Status and provenance

The source snapshot and evidence limits are recorded in [references/12-sources-and-provenance.md](references/12-sources-and-provenance.md). The Zuradio-specific lessons are stated as reusable defect-to-rule guidance in [references/11-zuradio-lessons.md](references/11-zuradio-lessons.md), with measured case-study results kept separate from universal requirements.

The completed realistic scaffold/design exercise is recorded in [tests/FORWARD_TEST.md](tests/FORWARD_TEST.md).

MIT licensed. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
