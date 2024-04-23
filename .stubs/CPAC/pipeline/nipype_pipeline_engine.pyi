"""Typing stubs for CPAC.pipeline.nipype_pipeline_engine."""

from pathlib import Path
from typing import Optional

from nipype.pipeline.engine import Workflow as NipypeWorkflow

class Workflow(NipypeWorkflow):
    def __init__(
        self: "Workflow",
        name: str,
        base_dir: Optional[Path | str] = None,
        debug: bool = False,
    ) -> None: ...
