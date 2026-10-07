# ARGOS Field Companion

**DEV Hacktoberfest 2026 — Open-Source AI Challenge, Week 1: Touch Grass**

ARGOS Field Companion is a new, offline-first project that turns an outdoor photo into a small real-world exploration mission. The goal is deliberately the opposite of an endless screen session: take one observation, let a local AI interpret it, then put the device away and investigate the physical environment.

## Flow

outdoor image → local vision backend → observation → safe field mission → JSONL field journal

The AI backend is isolated behind a tiny interface. The deterministic backend makes the project testable without a network connection; GemmaBackend is the integration boundary for a local Gemma vision runtime.

## Run

Run: python -m argos_field.cli path/to/outdoor-photo.jpg

## Test

Run: python -m pytest -q

## Open-source / prior-work disclosure

This repository was created as a new project during the Hacktoberfest 2026 Week 1 challenge window. It is inspired by the broader ARGOS multi-agent research project, but the Field Companion application, its challenge-specific architecture, code, tests, and documentation are developed in this repository for the challenge. Reused third-party components will be attributed as they are added.

## Safety

Missions are observational by design: do not disturb wildlife, damage plants, trespass, or enter unsafe areas.

## Next milestone

Connect a genuinely local Gemma vision runtime, add camera capture, record inference timing, and perform a documented outdoor field test.
