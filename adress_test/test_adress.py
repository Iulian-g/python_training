# -*- coding: utf-8 -*-

import pytest
from adress_model.adress import Adress
from adress_fixture.application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_adress_py(app):
        app.open_home_page()
        app.session.login(username="admin", password="secret")
        app.add_new()
        app.open_and_init_form_adress_book (Adress(firstname="gfhg", middlename="gfhf", lastname="fghfgh",
                                  nickname="fghfgh", title="fghfgh", company="fghfgh", address="fghfgh",
                                  home="fghfgh", mobile="fghfgh", work="fghfgh", fax="fghfgh", email="fghfgh",
                                  email2="fghfg", email3="fghfgh", homepage="fghfgh", address2="fghfg",
                                  phone2="fghfgh", notes="fghfgh"))
        app.return_to_home_page()
        app.session.logout()

def test_adress_empty_py(app):
            app.open_home_page()
            app.session.login(username="admin", password="secret")
            app.add_new()
            app.open_and_init_form_adress_book(Adress(firstname="", middlename="", lastname="",
                                                nickname="", title="", company="", address="",
                                                home="", mobile="", work="", fax="",
                                                email="",
                                                email2="", email3="", homepage="", address2="",
                                                phone2="", notes=""))
            app.return_to_home_page()
            app.session.logout()
