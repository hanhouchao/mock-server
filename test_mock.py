import pytest
import requests

host = "http://127.0.0.1:8080"


@pytest.mark.create
def test_create():
    print("start create================")
    path = "/api/tasks/"
    data = {"name": "test4", "desc": "test4", "id": 4}
    url = host + path
    res = requests.post(url, json=data)
    print(res.status_code)
    print(res.json())
    assert res.status_code == 201, "create error"


@pytest.mark.getall
def test_getall():
    print("start get all ================")
    path = "/api/tasks"
    url = host + path
    res = requests.get(url)
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200, "get error"


@pytest.mark.update
def test_update():
    print("start update================")
    path = "/api/tasks/test4"
    url = host + path
    data = {"name": "test4", "desc": "test41", "id": 4}
    res = requests.put(url, json=data)
    assert res.status_code == 204, "delete error"


@pytest.mark.get
def test_get():
    print("start get================")
    path = "/api/tasks/test4"
    url = host + path
    res = requests.get(url)
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200, "get error"


@pytest.mark.delete
def test_delete():
    print("start delete================")
    path = "/api/tasks/test4"
    url = host + path
    res = requests.delete(url)
    print(res.status_code)
    assert res.status_code == 204, "delete error"


@pytest.mark.getall
def test_get_delete_all():
    print("start get delete all ================")
    path = "/api/tasks"
    url = host + path
    res = requests.get(url)
    print(res.status_code)
    print(res.json())
    assert res.status_code == 200, "get error"
