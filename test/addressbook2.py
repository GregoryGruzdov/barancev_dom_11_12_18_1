# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(groupname="123", groupheader="123", groupfooter="123"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(Group(groupname="", groupheader="", groupfooter=""))
    app.logout()