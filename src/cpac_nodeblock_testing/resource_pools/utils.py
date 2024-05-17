# Copyright (C) 2024  C-PAC Developers

# This file is part of C-PAC.

# C-PAC is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.

# C-PAC is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
# License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with C-PAC. If not, see <https://www.gnu.org/licenses/>.

"""Utils for ResourcePools."""

from importlib.resources import as_file, files
from typing import Optional

from CPAC.pipeline.engine import ResourcePool
from CPAC.pipeline.nipype_pipeline_engine import Workflow
from CPAC.utils.configuration import Configuration
from CPAC.utils.test_init import create_dummy_node


def _validate_exclude(exclude: Optional[list[str] | str]) -> list[str]:
    """Coerce exclude argument to be a list of strings.

    Examples
    --------
    >>> _validate_exclude(exclude=100)
    Traceback (most recent call last):
    TypeError: 100 is <class 'int'> but list[str] is required.
    """
    if exclude is None:
        return []
    if isinstance(exclude, str):
        return [exclude]
    if not isinstance(exclude, list):
        msg = f"{exclude} is {type(exclude)} but list[str] is required."
        raise TypeError(msg)
    return exclude

def create_rpool(name, inputs, cfg, 
        exclude: Optional[list[str]] = None) -> tuple[Workflow, ResourcePool]:
    rpool = ResourcePool(name=name, cfg=cfg)
    wf = Workflow(name="brain_extraction_inputs")
    exclude = _validate_exclude(exclude)
    resources = [file for file in inputs if file not in exclude]
    node = create_dummy_node(name=name, fields=resources)
    with as_file(files("cpac_nodeblock_testing")) as repo:
        for resource in resources:
            setattr(
                node.inputs,
                resource,
                repo / f"data/anat/sub-1_ses-1_run-1_{resource}.nii.gz",
            )
            rpool.set_data(
                resource=resource,
                node=node,
                output=resource,
                json_info={},
                pipe_idx="",
                node_name=name,
            )
    return wf, rpool


