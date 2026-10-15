# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Any, Dict, List, Optional

from omegaconf import MISSING
from salix import Struct

from hydra.core.config_store import ConfigStore
from hydra.types import RunMode


class HelpConf(Struct, frozen=False):
    app_name: str = MISSING
    header: str = MISSING
    footer: str = MISSING
    template: str = MISSING


class HydraHelpConf(Struct, frozen=False):
    hydra_help: str = MISSING
    template: str = MISSING


class RunDir(Struct, frozen=False):
    dir: str = MISSING


class SweepDir(Struct, frozen=False):
    dir: str = MISSING
    subdir: str = MISSING


class OverridesConf(Struct, frozen=False):
    # Overrides for the hydra configuration
    hydra: List[str] = []
    # Overrides for the task configuration
    task: List[str] = []


# job runtime information will be populated here
class JobConf(Struct, frozen=False):
    # Job name, populated automatically unless specified by the user (in config or cli)
    name: str = MISSING

    # Change current working dir to the output dir.
    chdir: bool = False

    # Deprecated. Use the hydra_override_dirname resolver instead.
    override_dirname: str = "${hydra_override_dirname:}"

    # Job ID in underlying scheduling system
    id: str = MISSING

    # Job number if job is a part of a sweep
    num: int = MISSING

    # The config name used by the job
    config_name: Optional[str] = MISSING

    # Environment variables to set remotely
    env_set: Dict[str, str] = {}
    # Environment variables to copy from the launching machine
    env_copy: List[str] = []

    # Job config
    class JobConfig(Struct, frozen=False):
        # Default configuration for the ${hydra_override_dirname:} resolver.
        class OverrideDirname(Struct, frozen=False):
            kv_sep: str = "="
            item_sep: str = ","
            exclude_keys: List[str] = []

        override_dirname: OverrideDirname = OverrideDirname()

    config: JobConfig = JobConfig()


class ConfigSourceInfo(Struct, frozen=False):
    path: str
    schema: str
    provider: str


class RuntimeConf(Struct, frozen=False):
    version: str = MISSING
    version_base: str = MISSING
    cwd: str = MISSING
    config_sources: List[ConfigSourceInfo] = MISSING
    output_dir: str = MISSING

    # Composition choices dictionary
    # Ideally, the value type would be Union[str, List[str], None]
    choices: Dict[str, Any] = {}


class HydraConf(Struct, frozen=False):
    defaults: List[Any] = [
        {"output": "default"},
        {"launcher": "basic"},
        {"sweeper": "basic"},
        {"help": "default"},
        {"hydra_help": "default"},
        {"hydra_logging": "default"},
        {"job_logging": "default"},
        {"callbacks": None},
        # env specific overrides
        {"env": "default"},
    ]

    mode: Optional[RunMode] = None
    # Elements to append to the config search path.
    # Note: This can only be configured in the primary config.
    searchpath: List[str] = []

    # Normal run output configuration
    run: RunDir = RunDir()
    # Multi-run output configuration
    sweep: SweepDir = SweepDir()
    # Logging configuration for Hydra
    hydra_logging: Dict[str, Any] = MISSING
    # Logging configuration for the job
    job_logging: Dict[str, Any] = MISSING

    # Sweeper configuration
    sweeper: Any = MISSING
    # Launcher configuration
    launcher: Any = MISSING
    # Callbacks configuration
    callbacks: Dict[str, Any] = {}

    # Program Help template
    help: HelpConf = HelpConf()
    # Hydra's Help template
    hydra_help: HydraHelpConf = HydraHelpConf()

    # Output directory for produced configuration files and overrides.
    # E.g., hydra.yaml, overrides.yaml will go here. Useful for debugging
    # and extra context when looking at past runs.
    # Setting to None will prevent the creation of the output subdir.
    output_subdir: Optional[str] = ".hydra"

    # Those lists will contain runtime overrides
    overrides: OverridesConf = OverridesConf()

    job: JobConf = JobConf()

    # populated at runtime
    runtime: RuntimeConf = RuntimeConf()

    # Can be a boolean, string or a list of strings
    # If a boolean, setting to true will set the log level for the root logger to debug
    # If a string, it's interpreted as a the list [string]
    # If a list, each element is interpreted as a logger to have logging level set to debug.
    # Typical command lines to manipulate hydra.verbose:
    # hydra.verbose=true
    # hydra.verbose=[hydra,__main__]
    # TODO: good use case for Union support in OmegaConf
    verbose: Any = False


cs = ConfigStore.instance()

cs.store(
    group="hydra",
    name="config",
    node=HydraConf(),
    provider="hydra",
)
