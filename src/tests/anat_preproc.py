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
"""Tests for anatomical preprocessing."""

from typing import Optional

import pytest
from CPAC.anat_preproc.anat_preproc import brain_extraction
from CPAC.pipeline.cpac_pipeline import connect_pipeline
from CPAC.pipeline.engine import ResourcePool

from cpac_nodeblock_testing.resource_pools.anat_preproc import (
    _validate_exclude,
    BRAIN_EXTRACTION_CFG,
    brain_extraction_inputs,
)


@pytest.mark.parametrize(
    "exclude", [None, "desc-head_T1w", "desc-preproc_T1w", "space-T1w_desc-brain_mask"]
)
def test_brain_extraction(
    exclude: Optional[list[str]],
) -> None:
    """Test ~CPAC.anat_preproc.anat_preproc.brain_extraction connections."""

    def _run_test(
        exclude: Optional[list[str]],
        expected_exception: Optional[type[Exception]] = None,
    ) -> ResourcePool:
        """
        Run a test of the NodeBlock connections.

        Parameters
        ----------
        exclude
            list of resources to exclude from the input ResourcePool

        expceted_exception
            the exception we expect to raise given this ResourcePool
        """
        # TODO: generalize for reuse

        # Create Workflow and initial ResourcePool with inputs.
        wf, rpool = brain_extraction_inputs(exclude=exclude)

        # Make sure we don't already have all the outputs in the inputs.
        assert not all(
            [output in rpool.rpool for output in brain_extraction.outputs]
        ), "All outputs are present in the resource pool before connecting NodeBlock."

        # Make sure we catch missing required inputs.
        if expected_exception:
            with pytest.raises(expected_exception=expected_exception) as exception:
                connect_pipeline(wf, BRAIN_EXTRACTION_CFG, rpool, [brain_extraction])
            _e = str(exception.value)
            assert (
                "None of the listed resources are in the resource pool:" in _e
                and resource in _e
            ), f"{_e}\nC-PAC isn't complaining about missing resource {resource}."
            return

        # Connect the nodeblock(s).
        connect_pipeline(wf, BRAIN_EXTRACTION_CFG, rpool, [brain_extraction])

        # Return the updated ResourcePool.
        return rpool

    exclude = _validate_exclude(exclude)

    # Make sure required inputs raise LookupError when missing...
    for resource in ["desc-head_T1w", "space-T1w_desc-brain_mask"]:
        if resource in exclude:
            _run_test(exclude, LookupError)
            return
    # ...and LookupError isn't raised otherwise.
    rpool = _run_test(exclude)

    # Make sure all outputs from the connected NodeBlock are in the final ResourcePool
    try:
        assert all([output in rpool.rpool for output in brain_extraction.outputs])
    # Tell us which are missing if any are.
    except AssertionError:
        missing = []
        for output in brain_extraction.outputs:
            if output not in rpool.rpool:
                missing.append(output)
        msg = (
            "After connecting `brain_extraction`, still missing" f" outputs {missing}."
        )
        raise AssertionError(msg)
    return
