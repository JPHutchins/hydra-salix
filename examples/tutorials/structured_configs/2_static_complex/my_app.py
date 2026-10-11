# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class MySQLConfig(Struct, frozen=False):
    host: str = "localhost"
    port: int = 3306


class UserInterface(Struct, frozen=False):
    title: str = "My app"
    width: int = 1024
    height: int = 768


class MyConfig(Struct, frozen=False):
    db: MySQLConfig = MySQLConfig()
    ui: UserInterface = UserInterface()


cs = ConfigStore.instance()
cs.store(name="config", node=MyConfig)


@hydra.main(config_name="config")
def my_app(cfg: MyConfig) -> None:
    print(f"Title={cfg.ui.title}, size={cfg.ui.width}x{cfg.ui.height} pixels")


if __name__ == "__main__":
    my_app()
