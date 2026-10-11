# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from omegaconf import MISSING
from salix import Struct

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


def register_configs() -> None:
    cs = ConfigStore.instance()
    cs.store(
        group="database_lib/db",
        name="mysql",
        node=MySQLConfig,
    )
    cs.store(
        group="database_lib/db",
        name="postgresql",
        node=PostGreSQLConfig,
    )
