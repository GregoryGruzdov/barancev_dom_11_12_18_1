# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

# ОБУЧ.коммент: ГЛОБАЛЬНАЯ ПЕРЕМЕННАЯ, назвали в честь того, что там мы будем хранить фикстуру между тестами(мы убрали из @pytest.fixture параметр сессии, и теперь браузер запускатсся каждый раз
fixture = None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
