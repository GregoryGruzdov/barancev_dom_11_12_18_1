from model.group import Group

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group_name(Group(groupname="SISKA"))
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group_header(Group(groupheader="SISKA"))
    app.session.logout()

