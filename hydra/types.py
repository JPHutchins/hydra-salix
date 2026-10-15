# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from enum import Enum
from typing import TYPE_CHECKING, Any, Callable

from salix import Struct

TaskFunction = Callable[[Any], Any]


if TYPE_CHECKING:
    from hydra._internal.callbacks import Callbacks
    from hydra.core.config_loader import ConfigLoader


class HydraContext(Struct, frozen=False):
    config_loader: "ConfigLoader"
    callbacks: "Callbacks"
    execution_whitelist: Any = None


class RunMode(Enum):
    RUN = 1
    MULTIRUN = 2


class ConvertMode(Enum):
    """ConvertMode for instantiate, controls return type.

    A config is either config or instance-like (`_target_` field).

    If instance-like, instantiate resolves the callable (class or
    function) and returns the result of the call on the rest of the
    parameters.

    If "none", config-like configs will be kept as is.

    If "partial", config-like configs will be converted to native python
    containers (list and dict), unless they are structured configs (
    Struct instances). Structured configs remain as DictConfig objects.

    If "object", config-like configs will be converted to native python
    containers (list and dict), unless they are structured configs (
    Struct instances). Structured configs are converted to instances
    of the backing Struct class using OmegaConf.to_object.

    If "all", config-like configs will all be converted to native python
    containers (list and dict).
    """

    # Use DictConfig/ListConfig
    NONE = "none"
    # Convert the OmegaConf config to primitive container, Structured Configs are preserved
    PARTIAL = "partial"
    # Convert the OmegaConf config to primitive container, Structured Configs are converted to
    # Struct instances.
    OBJECT = "object"
    # Fully convert the OmegaConf config to primitive containers (dict, list and primitives).
    ALL = "all"

    def __eq__(self, other: Any) -> Any:
        if isinstance(other, ConvertMode):
            return other.value == self.value
        elif isinstance(other, str):
            return other.upper() == self.name.upper()
        else:
            return NotImplemented
