"""Typing stubs for nipype.pipeline.engine."""

from pathlib import Path
from typing import Any, Generator, Optional

from nipype.interfaces.base import DynamicTraitedSpec, Interface
from nipype.pipeline.engine.base import EngineBase

class Node(EngineBase):
    def __init__(
        self: "Node",
        interface: Interface,
        name: str,
        iterables: Optional[Generator] = None,
        itersource: Optional[tuple] = None,
        synchronize: bool = False,
        overwrite: Optional[bool] = None,
        needed_outputs: Optional[list[str]] = None,
        run_without_submitting: bool = False,
        n_procs: Optional[int] = None,
        mem_gb: float = 0.20,
        **kwargs: Any,  # noqa: ANN401,
    ) -> None: ...
    @property
    def inputs(self: "Node") -> DynamicTraitedSpec: ...

class Workflow(EngineBase):
    def __init__(
        self: "Workflow", name: str, base_dir: Optional[Path | str]
    ) -> None: ...
