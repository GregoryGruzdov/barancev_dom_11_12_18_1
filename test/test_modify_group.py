from model.group import Group


def test_modify_group_name(app):
    app.group.prepare_groups()
    app.group.modify_first_group(Group(groupname="name"))


def test_modify_group_header(app):
    app.group.prepare_groups()
    app.group.modify_first_group(Group(groupheader="header"))

