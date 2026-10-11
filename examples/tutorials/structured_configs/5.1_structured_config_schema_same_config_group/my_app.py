# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from omegaconf import MISSING, OmegaConf
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


class PostGreSQLConfig(DBConfig, frozen=False):
    driver: str = "postgresql"
    user: str = MISSING
    port: int = 5432
    password: str = MISSING
    timeout: int = 10


class Config(Struct, frozen=False):
    db: DBConfig = MISSING
    debug: bool = False


cs = ConfigStore.instance()
cs.store(name="base_config", node=Config)
cs.store(group="db", name="base_mysql", node=MySQLConfig)
cs.store(group="db", name="base_postgresql", node=PostGreSQLConfig)


@hydra.main(config_path="conf", config_name="config")
def my_app(cfg: Config) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()
