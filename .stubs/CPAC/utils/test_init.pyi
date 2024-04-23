"""Typing stubs for CPAC.utils.test_init."""

from typing import Optional

from nipype.pipeline.engine import Node

def create_dummy_node(name: str, fields: Optional[list[str]] = None) -> Node: ...
