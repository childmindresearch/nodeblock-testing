"""Typing stubs for nipype.pipeline.engine.base."""

from pathlib import Path
from typing import Optional

class EngineBase:
    def __init__(
        self: "EngineBase",
        name: Optional[str] = None,
        base_dir: Optional[Path | str] = None,
    ) -> None: ...
