#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_base
----------------------------------

Tests for `tedega_core.model.base` module.
"""
from tedega_storage import RDBMSStorageBase
from tedega_core.model.base import BaseItem
from tedega_core.model.mixins import Protocol


class Dummy(Protocol, BaseItem, RDBMSStorageBase):
    __tablename__ = "base"


def test_create_base(storage):
    import uuid
    import datetime
    factory = Dummy.get_factory(storage)
    base = factory.create()
    assert base.id is None
    assert isinstance(base.uuid, uuid.UUID)
    assert isinstance(base.created, datetime.datetime)
    assert isinstance(base.updated, datetime.datetime)
    assert isinstance(base.__json__(), dict)
