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
"""ResourcePool storage."""

from typing import Optional, Union

from CPAC.pipeline.engine import ResourcePool

_KEY_TYPE = list[str] | tuple[str, ...]
_POOL_KEY_TYPE = dict[tuple[str, ...], ResourcePool]


class ResourcePoolPool:
    """Dictionary-like object to store and retrieve ResourcePools."""

    def __init__(self, rpools: Optional[_POOL_KEY_TYPE] = None):
        self.rpools = (
            {}
            if rpools is None
            else {self._sort_key(item[0]): item[1] for item in rpools.items()}
        )

    def __add__(
        self, other: Union[_POOL_KEY_TYPE, "ResourcePoolPool"]
    ) -> "ResourcePoolPool":
        """Add a ResourcePool to a ResourcePoolPool or combine two ResourcePoolPools."""
        if isinstance(other, ResourcePoolPool):
            return ResourcePoolPool({**self.rpools, **other.rpools})
        else:
            return ResourcePoolPool({**self.rpools, **other})

    def __get__(self, key: _KEY_TYPE) -> ResourcePool:
        """Get a ResourcePool by list or tuple of resources."""
        return self.rpools[self._sort_key(key)]

    def __iadd__(
        self, other: Union[_POOL_KEY_TYPE, "ResourcePoolPool"]
    ) -> "ResourcePoolPool":
        """Add a ResourcePool to a ResourcePoolPool or combine two ResourcePoolPools."""
        if isinstance(other, ResourcePoolPool):
            self.rpools.update(other.rpools)
        else:
            self.rpools.update(other)
        return self

    def __repr__(self) -> str:
        """Return reproducible string representation of ResourcePoolPool."""
        return f"ResourcePoolPool({self.rpools})"

    @staticmethod
    def _sort_key(key: _KEY_TYPE) -> tuple[str, ...]:
        """Return a sorted tuple of a list or tuple of resource keys."""
        key_list: list[str] = list(key)
        key_list.sort()
        return tuple(key_list)

    def __str__(self) -> str:
        """Return string representation of ResourcePoolPool."""
        return str(list(self.rpools.keys()))


# def rp_factory(keys: _KEY_TYPE, module: Path) -> ResourcePool:
#     """Given a list of resource keys, return a ResourcePool with all of them."""
#     existing_pickle_path = module / "existing.pkl"
#     if existing_pickle_path.exists():
#         with open("existing.pkl", "rb") as _existing:
#             resource_pools: ResourcePoolPool = pickle.load(_existing)
#     else:
#         resource_pools = ResourcePoolPool()
#     keys, resource_pools  # TODO finish this factory
