"""Typing stubs for CPAC.pipeline.cpac_pipeline."""

from nipype.pipeline.engine import Workflow
from CPAC.pipeline.engine import ResourcePool
from CPAC.pipeline.nodeblock import NodeBlockFunction
from CPAC.utils.configuration import Configuration

def connect_pipeline(
    wf: Workflow,
    cfg: Configuration,
    rpool: ResourcePool,
    pipeline_blocks: list[NodeBlockFunction],
) -> Workflow: ...
