# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

from omegaconf import MISSING, DictConfig
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class TestConfig(Struct, frozen=False):
    param: int = MISSING


config_store = ConfigStore.instance()
config_store.store(group="test", name="default", node=TestConfig)


@hydra.main(config_path=".", config_name="config")
def run(config: DictConfig) -> None:
    print(config.test.param)


if __name__ == "__main__":
    run()
