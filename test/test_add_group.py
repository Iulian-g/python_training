# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_py(app):
        app.group.create(Group(name="new name", header="new header", footer="new footer"))

def test_add_empty_group_py(app):
        app.group.create(Group(name="", header="", footer=""))



