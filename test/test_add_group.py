# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application



@pytest.fixture
def app(request):
        fixture = Application()
        request.addfinalizer(fixture.destroy)
        return fixture


def test_add_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create_group(Group(name="new", header="new", footer="new"))
        app.session.logout()


def test_add_empty_group_py(app):
        app.session.login(username="admin", password="secret")
        app.group.create_group(Group(name="", header="", footer=""))
        app.session.logout()
