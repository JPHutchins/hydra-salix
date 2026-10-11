# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Any

from omegaconf import OmegaConf
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class MySQLConfig(Struct, frozen=False):
    driver: str = "mysql"
    host: str = "localhost"
    port: int = 3306


class PostGreSQLConfig(Struct, frozen=False):
    driver: str = "postgresql"
    host: str = "localhost"
    port: int = 5432
    timeout: int = 10


class Config(Struct, frozen=False):
    # We will populate db using composition.
    db: Any


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)


@hydra.main(config_name="config")
def my_app(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
