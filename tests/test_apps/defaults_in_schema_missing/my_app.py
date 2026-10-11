# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Any, List

from omegaconf import MISSING, DictConfig, OmegaConf
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class DBConfig(Struct, frozen=False):
    driver: str = MISSING
    host: str = "localhost"
    port: int = MISSING


class MySQLConfig(DBConfig, frozen=False):
    driver: str = "mysql"
    port: int = 3306
    user: str = MISSING
    password: str = MISSING


class Config(Struct, frozen=False):
    defaults: List[Any] = MISSING
    db: DBConfig = MISSING


cs = ConfigStore.instance()
cs.store(group="db", name="mysql", node=MySQLConfig, provider="main")
cs.store(name="config", node=Config, provider="main")


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
