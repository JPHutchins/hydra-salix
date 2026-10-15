# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from typing import Any

from omegaconf import MISSING
from salix import Struct

from hydra.core.config_store import ConfigStore


class ConfigWithoutGroup(Struct, frozen=False):
    group: bool = False


class ConfigWithUnicode(Struct, frozen=False):
    group: str = "数据库"


class Cifar10(Struct, frozen=False):
    name: str = "cifar10"
    path: str = "/datasets/cifar10"


class ImageNet(Struct, frozen=False):
    name: str = "imagenet"
    path: str = "/datasets/imagenet"


class ConfigWithoutExt(Struct, frozen=False):
    foo: str = "bar"


class Adam(Struct, frozen=False):
    type: str = "adam"
    lr: float = 0.1
    beta: float = 0.01


class Nesterov(Struct, frozen=False):
    type: str = "nesterov"
    lr: float = 0.001


class Optimizer(Struct, frozen=False):
    optimizer: Any = MISSING


s = ConfigStore.instance()
s.store(name="config_without_group", node=ConfigWithoutGroup)
s.store(name="config_with_unicode", node=ConfigWithUnicode)
s.store(name="dataset", node={"dataset_yaml": True})
s.store(group="dataset", name="cifar10", node=Cifar10)
s.store(group="dataset", name="imagenet.yaml", node=ImageNet)
s.store(group="optimizer", name="adam", node=Adam)
s.store(group="optimizer", name="nesterov", node=Nesterov)
s.store(group="level1/level2", name="nested1", node={"l1_l2_n1": True})
s.store(group="level1/level2", name="nested2", node={"l1_l2_n2": True})
s.store(group="package_test", name="none", node={"foo": "bar"}, package=None)
s.store(group="package_test", name="explicit", node={"foo": "bar"}, package="a.b")
s.store(group="package_test", name="global", node={"foo": "bar"}, package="_global_")
s.store(group="package_test", name="group", node={"foo": "bar"}, package="_group_")
s.store(
    group="package_test",
    name="group_name",
    node={"foo": "bar"},
    package="foo._group_._name_",
)
s.store(group="package_test", name="name", node={"foo": "bar"}, package="_name_")
s.store(name="primary_config", node={"primary": True}, package=None)
s.store(
    name="primary_config_with_non_global_package", node={"primary": True}, package="foo"
)

s.store(
    name="config_with_defaults_list",
    node={
        "defaults": [{"dataset": "imagenet"}],
        "key": "value",
    },
)

s.store(
    group="configs_with_defaults_list",
    name="global_package",
    node={
        "defaults": [{"foo": "bar"}],
        "x": 10,
    },
    package="_global_",
)

s.store(
    group="configs_with_defaults_list",
    name="group_package",
    node={
        "defaults": [{"foo": "bar"}],
        "x": 10,
    },
    package="_group_",
)
