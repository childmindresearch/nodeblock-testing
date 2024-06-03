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
"""ResourcePools for registration."""

from cpac_nodeblock_testing.resource_pools.utils import load_rpool

COREG_CFG = ["registration_workflows", {"functional_registration": {"coregistration": {"run": True, "Reference": "brain"}}}]


COREG_RESOURCES = [
        (
            "sbref",
            "desc-motion_bold",
            "space-bold_label-WM_mask",
            "despiked-fieldmap",
            "fieldmap-mask",
            "effectiveEchoSpacing",
            "pe-direction",
        ),
        (
            "desc-preproc_T1w",
            "desc-restore-brain_T1w",
            "desc-preproc_T2w",
            "desc-preproc_T2w",
            "T2w",
            ["label-WM_probseg", "label-WM_mask"],
            ["label-WM_pveseg", "label-WM_mask"],
            "desc-head_T1w",
            "desc-head_T2w",
        ),
]

def coreg_inputs(cfg, wf, rpool, exclude=None):
    wf, rpool = load_rpool(cfg, wf, rpool, name="coreg_inputs", inputs=COREG_RESOURCES, 
            exclude=None)
    return wf, rpool