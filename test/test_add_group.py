# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_py(app):
        old_group = app.group.get_group_list( )
        app.group.create(Group(name="new name", header="new header", footer="new footer"))
        new_group = app.group.get_group_list( )
        assert len(old_group) + 1 == len(new_group)


def test_add_empty_group_py(app):
        old_group = app.group.get_group_list( )
        app.group.create(Group(name="", header="", footer=""))
        new_group = app.group.get_group_list( )
        assert len(old_group) + 1 == len(new_group)




