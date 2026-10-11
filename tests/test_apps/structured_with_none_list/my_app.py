# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import List, Optional

from omegaconf import DictConfig
from salix import Struct

import hydra
from hydra.core.config_store import ConfigStore


class Config(Struct, frozen=False):
    list: Optional[List[int]] = None


cs = ConfigStore.instance()
cs.store(name="config", node=Config)


@hydra.main(config_name="config")
def main(cfg: DictConfig) -> None:
    print(cfg)


if __name__ == "__main__":
    main()
