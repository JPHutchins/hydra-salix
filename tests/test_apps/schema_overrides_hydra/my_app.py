# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Dict

from omegaconf import MISSING
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore
from hydra.core.hydra_config import HydraConfig


class Config(Struct, frozen=False):
    age: int = MISSING
    name: str = MISSING
    group: Dict[str, str] = MISSING


ConfigStore.instance().store(name="config_schema", node=Config)


@hydra.main(config_path=".", config_name="config")
def my_app(cfg: Config) -> None:
    print(
        f"job_name: {HydraConfig().get().job.name}, "
        f"name: {cfg.name}, age: {cfg.age}, group: {cfg.group['name']}"
    )


if __name__ == "__main__":
    my_app()
