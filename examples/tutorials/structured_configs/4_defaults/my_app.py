# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Any, List

from omegaconf import MISSING, OmegaConf
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class MySQLConfig(Struct, frozen=False):
    driver: str = "mysql"
    host: str = "localhost"
    port: int = 3306
    user: str = "omry"
    password: str = "secret"


class PostGreSQLConfig(Struct, frozen=False):
    driver: str = "postgresql"
    host: str = "localhost"
    port: int = 5432
    timeout: int = 10
    user: str = "postgres_user"
    password: str = "drowssap"


defaults = [
    # config group name db will load config named mysql
    {"db": "mysql"}
]


class Config(Struct, frozen=False):
    defaults: List[Any] = defaults

    # Hydra will populate this field based on the defaults list
    db: Any = MISSING


cs = ConfigStore.instance()
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)
cs.store(name="config", node=Config)


@hydra.main(config_name="config")
def my_app(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
