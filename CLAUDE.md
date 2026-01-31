# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pygentic-code is a multi-agent code generation framework using Anthropic's Claude Agent SDK. It implements a 5-phase pipeline: Research → Plan → Detail Plan → Code → Review. Each phase is handled by a dedicated agent with specific tools and prompts.

## Architecture

### Agent Pipeline

The **Orchestrator** (`orchestrator.py`) drives 5 sequential phases:

1. **ResearcherAgent** — Analyzes requirements, searches codebase/web. Outputs markdown to `research/`.
2. **PlannerAgent** — Creates high-level implementation plan from research. Outputs to `plans/`.
3. **DetailPlannerAgent** — Breaks plans into ordered, self-contained tasks. Outputs to `detail_plans/`.
4. **CoderAgent** — Implements code following a TODO checklist pattern. Uses `acceptEdits` permission mode.
5. **ReviewerAgent** — Reviews code for conventions, quality, bugs, security. Outputs JSON to `reviews/`.

Each agent is defined in `src/code_agent_by_claude/agents/` with a corresponding system prompt and task template in `agents/prompts/` (markdown files loaded at runtime via `prompts/__init__.py`).

### Event/Streaming System

- `events.py` — Typed event classes (TextEvent, ToolEvent, ThinkingEvent, PhaseEvent, etc.)
- `stream_handler.py` — Dispatches events to callbacks; DefaultStreamRenderer handles CLI output
- `message_processor.py` — Converts Claude Agent SDK messages into typed events

### Data Flow

Agent outputs use typed dataclasses: `ResearchResult`, `Plan`, `CodeResult`, `ReviewResult`, all aggregated into `TaskResult`. Result parsing extracts JSON blocks from agent responses with regex fallback.

## Code Style

- Line length: 80 characters (ruff)
- Python target: 3.12+
- Package uses src layout (`src/code_agent_by_claude/`)
