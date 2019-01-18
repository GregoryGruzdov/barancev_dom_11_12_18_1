# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(groupname="123", groupheader="123", groupfooter="123"))


def test_add_empty_group(app):
    app.group.create(Group(groupname="", groupheader="", groupfooter=""))

