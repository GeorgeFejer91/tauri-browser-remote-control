# Repository instructions

> Mandatory first read: [for-ai/README.md](./for-ai/README.md). It is the YAGNI control-plane router; then follow the project-specific rules below.

Read `SKILL.md` and the references relevant to the requested change before editing.

Preserve the core boundary: one Rust authority, typed application actions, separate control/state/bulk lanes, explicit authentication and authorization, bounded resources, and evidence-based completion claims.

Run the repository checks documented in `README.md` after every material change. Changes to protocol contracts, authentication guidance, transfer framing, starter code, or qualification requirements also require a realistic forward test using the scaffold script.

Do not describe an application as production-ready because this skill validates. Application completion requires the real browser/native qualification gate in `references/10-qualification.md`.

<!-- for-ai:shared-skills:start -->
## Shared project workflow

At project entry, also read [for-ai/SKILLS.md](for-ai/SKILLS.md) for the required RTK, GSD Core,
and Superpowers baseline, conditional Rust/Tauri/HTML routes, and Git worktree
policy. Preserve this project's product and evidence contracts.

Read the durable project goal and resume its active checklist at session
start. Before ending, update that same state with evidence, blockers, the
next action, and observed Git/publication state. Keep the overall goal open
until its own acceptance criteria pass.
<!-- for-ai:shared-skills:end -->
