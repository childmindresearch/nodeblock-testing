"""Typing stubs for CPAC.utils.configuration."""

from typing import Any, Optional

class Configuration:
    def __init__(
        self: "Configuration",
        config_map: Optional[dict[str, Any]] = None,
        skip_env_check: bool = False,
    ) -> None: ...
