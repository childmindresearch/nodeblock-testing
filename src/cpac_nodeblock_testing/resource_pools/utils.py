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

from nipype.pipeline.engine import Node
from CPAC.pipeline.engine import ResourcePool
from CPAC.pipeline.nipype_pipeline_engine import Workflow
from CPAC.utils.test_init import create_dummy_node


class Resource:
    """Class to determine resource path and type."""

    def __init__(self, resource: str) -> None:
        """Find the resource and its type."""
        self.key = resource
        """Resource key string."""
        with as_file(files("cpac_nodeblock_testing")) as repo:
            for resource_type in ["anat", "fmap", "func"]:
                resource_path = (
                    repo / f"data/{resource_type}/sub-1_ses-1_run-1_{resource}.nii.gz"
                )
                if resource_path.exists():
                    self.path = resource_path
                    """Path to Resource."""
                    self.type = resource_type
                    """Type of Resource."""
                    break  # store first match and stop
        if not hasattr(self, "path"):
            raise FileNotFoundError(resource)


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


def initialize_rpool(cfg) -> tuple[Workflow, ResourcePool]:
    wf = Workflow(name="load_resources")
    rpool = ResourcePool(name="load_rpool", cfg=cfg)
    return wf, rpool


def load_rpool(
    cfg, wf, rpool, name, inputs, exclude: Optional[list[str]] = None
) -> tuple[Workflow, ResourcePool]:
    exclude = _validate_exclude(exclude)
    resources = [file for file in inputs if file not in exclude]
    resources = [item[0] if isinstance(item, tuple) else item for item in resources]
    resources.append("scan")
    node = create_dummy_node(name=name, fields=resources)
    node.scan = "task-rest"
    rpool.set_data("scan", node, "scan", {}, "", "func_ingress")

    for resource in resources:
        if isinstance(resource, tuple):
            for item in resource:
                rpool = load_resource(item, name, node, rpool)
        else:
            rpool = load_resource(resource, name, node, rpool)

    return wf, rpool


def load_resource(key: str, name: str, node: Node, rpool: ResourcePool) -> ResourcePool:
    resource = Resource(key)
    # Want to pass {subdir} as arg
    if resource.type == "func":
        # if subdir == func, add scan name to resource name
        pass
    setattr(
        node.inputs,
        resource.key,
        resource.path,
    )
    rpool.set_data(
        resource=resource.key,
        node=node,
        output=resource.key,
        json_info={},
        pipe_idx="",
        node_name=name,
    )
    return rpool