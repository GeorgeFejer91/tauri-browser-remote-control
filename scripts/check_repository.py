#!/usr/bin/env python3
"""Deterministic structural checks for the skill and reusable starter."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "README.md",
    "LICENSE",
    "THIRD_PARTY_NOTICES.md",
    "references/00-system-contract.md",
    "references/10-qualification.md",
    "references/11-zuradio-lessons.md",
    "references/12-sources-and-provenance.md",
    "references/13-tauri-application-foundation.md",
    "assets/starter/contracts/application-profile.schema.json",
    "assets/starter/contracts/application-profile.example.json",
    "assets/starter/contracts/wire-envelope.schema.json",
    "assets/starter/contracts/wire-envelope.example.json",
    "assets/starter/contracts/remembered-device-record.schema.json",
    "assets/starter/contracts/transfer-manifest.schema.json",
    "assets/starter/contracts/transfer-manifest.example.json",
    "assets/starter/rust/Cargo.toml",
    "assets/starter/browser/package.json",
    "assets/templates/VERIFICATION-GATE.md",
]


def local_markdown_targets(path: Path) -> list[Path]:
    targets: list[Path] = []
    for raw in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
        target = raw.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0])
        targets.append((path.parent / target).resolve())
    return targets


def frontmatter(skill: str) -> tuple[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md is missing YAML frontmatter")
    name_match = re.search(r"^name:\s*(.+)$", match.group(1), re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+)$", match.group(1), re.MULTILINE)
    if not name_match or not description_match:
        raise ValueError("SKILL.md frontmatter needs name and description")
    return name_match.group(1).strip(), description_match.group(1).strip()


def validate_profile(profile: dict[str, object]) -> list[str]:
    errors: list[str] = []
    authority = profile.get("authority")
    authentication = profile.get("authentication")
    transports = profile.get("transports")
    privacy = profile.get("privacy")
    if not isinstance(authority, dict) or authority.get("owner") != "rust":
        errors.append("example profile must make Rust authoritative")
    remembered = authentication.get("rememberedBrowser") if isinstance(authentication, dict) else None
    if not isinstance(remembered, dict) or remembered.get("maximumTtlSeconds", 86_401) > 86_400:
        errors.append("remembered-browser example must expire within 24 hours")
    if not isinstance(transports, dict) or transports.get("bulkLane") != "reliable-ordered-binary":
        errors.append("example profile must define a separate binary bulk lane")
    if not isinstance(privacy, dict) or any(
        privacy.get(field) is not False
        for field in ("staticHostContainsUserData", "nativePathsOnWire", "secretsInUrls")
    ):
        errors.append("example profile violates the static/privacy boundary")
    return errors


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        try:
            name, description = frontmatter(skill)
            if name != "tauri-browser-remote-control":
                errors.append("unexpected skill name")
            if not (80 <= len(description) <= 1024):
                errors.append("skill description is not sufficiently discriminating")
        except ValueError as error:
            errors.append(str(error))
        for required in ("one Rust authority", "PAKE", "24-hour", "bulk", "qualification"):
            if required.lower() not in skill.lower():
                errors.append(f"SKILL.md is missing required concept: {required}")

    yaml_path = ROOT / "agents" / "openai.yaml"
    if yaml_path.is_file():
        yaml = yaml_path.read_text(encoding="utf-8")
        if "$tauri-browser-remote-control" not in yaml:
            errors.append("openai.yaml default prompt must name the skill")
        match = re.search(r'^\s*short_description:\s*"([^"]+)"', yaml, re.MULTILINE)
        if not match or not (25 <= len(match.group(1)) <= 64):
            errors.append("openai.yaml short_description must be 25-64 characters")

    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as error:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {error}")

    profile_path = ROOT / "assets/starter/contracts/application-profile.example.json"
    if profile_path.is_file():
        profile = json.loads(profile_path.read_text(encoding="utf-8"))
        errors.extend(validate_profile(profile))

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "[TODO" in text or "TODO:" in text:
            errors.append(f"unresolved TODO marker in {path.relative_to(ROOT)}")
        for target in local_markdown_targets(path):
            try:
                target.relative_to(ROOT)
            except ValueError:
                errors.append(f"local link escapes repository in {path.relative_to(ROOT)}: {target}")
                continue
            if not target.exists():
                errors.append(f"broken local link in {path.relative_to(ROOT)}: {target.relative_to(ROOT)}")

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
