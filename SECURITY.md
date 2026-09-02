# Security policy

Please report suspected vulnerabilities privately through GitHub's security advisory flow rather than a public issue.

Security-sensitive areas include authentication transcripts, remembered-device proofs, scope enforcement, generation/revocation behavior, command deduplication, binary framing, transfer integrity, loopback bootstrap secrets, Tauri capabilities, signaling metadata, and service supervision.

This repository is guidance and starter material, not a deployed service. A generated application must select maintained cryptographic implementations, threat-model its exact topology, and pass its own installed browser/device/network qualification matrix.
