"""Typing stubs for nipype.interfaces.base."""

from typing import Optional

from traits.api import HasTraits

class BaseTraitedSpec(HasTraits): ...
class DynamicTraitedSpec(BaseTraitedSpec): ...

class Interface:
    input_spec: Optional[HasTraits] = None
    output_spec: Optional[HasTraits] = None
    @property
    def can_resume(self) -> bool: ...
    @property
    def always_run(self) -> bool: ...
    @property
    def version(self) -> str: ...
