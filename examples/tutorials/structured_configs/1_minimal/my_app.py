# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class MySQLConfig(Struct, frozen=False):
    host: str = "localhost"
    port: int = 3306


cs = ConfigStore.instance()
# Registering the Config class with the name 'config'.
cs.store(name="config", node=MySQLConfig)


@hydra.main(config_name="config")
def my_app(cfg: MySQLConfig) -> None:
    print(f"Host: {cfg.host}, port: {cfg.port}")


if __name__ == "__main__":
    my_app()
