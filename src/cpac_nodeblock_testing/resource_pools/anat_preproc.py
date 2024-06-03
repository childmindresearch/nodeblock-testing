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
"""ResourcePools for anatomical preprocessing."""

from importlib.resources import as_file, files
from typing import Optional
import os

from CPAC.pipeline.engine import ResourcePool
from CPAC.pipeline.nipype_pipeline_engine import Workflow
from CPAC.utils.configuration import Configuration
from CPAC.utils.test_init import create_dummy_node
from cpac_nodeblock_testing.resource_pools.utils import (
    load_rpool,
    _validate_exclude,
)

BRAIN_EXTRACTION_CFG = ["anatomical_preproc", {"brain_extraction": {"run": True}, "run": True}]

BRAIN_EXTRACTION_RESOURCES = [
            "desc-head_T1w",
            "desc-preproc_T1w",
            "space-T1w_desc-brain_mask",
        ]

def brain_extraction_inputs(CFG, wf, rpool, exclude=None):
    
    wf, rpool = load_rpool(CFG, wf, rpool, name="brain_extraction_inputs", inputs=BRAIN_EXTRACTION_RESOURCES, 
            exclude=None)
    return wf, rpool