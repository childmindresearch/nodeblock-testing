"""Type stubs for CPAC.pipeline.engine."""

from typing import Any, Optional

from nipype.pipeline.engine import Node
from CPAC.utils.configuration import Configuration

class ResourcePool:
    rpool: dict | "ResourcePool"
    def __init__(
        self: "ResourcePool",
        rpool: Optional["ResourcePool"] = None,
        name: Optional[str] = None,
        cfg: Optional[Configuration | dict] = None,
        pipe_list: Optional[list[Any]] = None,
    ) -> None: ...
    def get_entire_rpool(self: "ResourcePool") -> dict: ...
    def set_data(
        self: "ResourcePool",
        resource: str,
        node: Node,
        output: str,
        json_info: dict[str, Any],
        pipe_idx: str | int,
        node_name: str,
        fork: bool = False,
        inject: bool = False,
    ) -> None: ...
