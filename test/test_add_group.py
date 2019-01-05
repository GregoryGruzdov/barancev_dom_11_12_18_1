# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="123", groupheader="123", groupfooter="123"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="", groupheader="", groupfooter=""))
    app.session.logout()
