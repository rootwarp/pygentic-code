"""AI Coding Agents using Claude Agent SDK."""

from .agents import CoderAgent, DetailPlannerAgent, PlannerAgent, ReviewerAgent
from .agents.coder import CodeResult
from .agents.planner import Plan
from .agents.reviewer import ReviewResult
from .events import (
    EventType,
    PhaseEvent,
    ProgressEvent,
    StreamEvent,
    TextEvent,
    ThinkingEvent,
    ToolEvent,
)
from .message_processor import MessageProcessor
from .orchestrator import (
    Orchestrator,
    TaskResult,
    run_coding_task,
    run_coding_task_with_stream,
)
from .stream_handler import DefaultStreamRenderer, StreamHandler

__version__ = "0.1.0"
__all__ = [
    "PlannerAgent",
    "DetailPlannerAgent",
    "CoderAgent",
    "ReviewerAgent",
    "Plan",
    "CodeResult",
    "ReviewResult",
    "Orchestrator",
    "TaskResult",
    "run_coding_task",
    "run_coding_task_with_stream",
    "EventType",
    "StreamEvent",
    "TextEvent",
    "ToolEvent",
    "ThinkingEvent",
    "PhaseEvent",
    "ProgressEvent",
    "StreamHandler",
    "DefaultStreamRenderer",
    "MessageProcessor",
]
