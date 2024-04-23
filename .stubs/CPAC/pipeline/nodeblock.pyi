"""Typing stubs for CPAC.pipeline.nodeblock."""

from typing import Any, Callable, Optional

class NodeBlockFunction:
    outputs: list[str] | dict[str, Any]
    def __init__(
        self,
        func: Callable,
        name: Optional[str] = None,
        config: Optional[list[str]] = None,
        switch: Optional[list[str] | list[list[str]]] = None,
        option_key: Optional[str | list[str]] = None,
        option_val: Optional[str | list[str]] = None,
        inputs: Optional[list[str | list | tuple]] = None,
        outputs: Optional[list[str] | dict[str, Any]] = None,
    ) -> None: ...
