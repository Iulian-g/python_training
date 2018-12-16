# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="new", header="new", footer="new"))
        app.session.logout()

def test_add_empty_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create(Group(name="", header="", footer=""))
        app.session.logout()
