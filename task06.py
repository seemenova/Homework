"""
Протестировать API.
Можно взять одно из двух на выбор:
https://dummy.restapiexample.com/
https://reqres.in/

Необходимо написать не менее пяти тестов.
Протестировать как методы GET, так и пост POST.
При создании тестов использовать фикстуры.

"""
import pytest
import requests
from pydantic import BaseModel

# class Employee(BaseModel):
#     status: str
#     data: str
#     id: str
#     employee_name: str
#     employee_salary: str
#     employee_age: str
#     profile_image: str
#
#
# @pytest.fixture
# def url():
#     return "https://dummy.restapiexample.com/"
#
# @pytest.fixture
# def employee_url():
#     return "http://dummy.restapiexample.com/api/v1/employee"
#
# @pytest.fixture
# def employees_url():
#     return 	"http://dummy.restapiexample.com/api/v1/employees"
#
# @pytest.fixture
# def params_id_get():
#     return {'id': 14}
#
#
# def test_positive_get(url):
#     """
#     Проверяем, что имеется доступ по указанному url
#     """
#     r = requests.get(url, headers={"User-Agent": "Test06"}, verify = False)
#     assert r.status_code == requests.codes.ok
#
#
# def test_get_employee_name(employees_url, params_id_get):
#     r = requests.get(employees_url, headers={"User-Agent": "Test06"}, verify = False, params = params_id_get)
#     x = r.json()
#     assert r.url == "https://dummy.restapiexample.com/api/v1/employee/14"
#     assert x['data']['employee_name'] == "https://dummy.restapiexample.com/api/v1/employee/14"
#
# # def test_negative_get():

@pytest.fixture
def url():
    return "https://reqres.in/api/users"

@pytest.fixture
def params_page_get():
    return {"page": 2}

@pytest.fixture
def params_id_get():
    return {"id": 4}

@pytest.fixture
def params_user_post():
    return {"name": "Ostin", "job": "Manager"}

def test_get_positive(url):
    """
    Проверяем, что имеется доступ по указанному url
    """
    r = requests.get(url, verify = False)
    assert r.status_code == requests.codes.ok

def test_get_count_records_on_page(url, params_page_get):
    """
    Проверяем, что количество записей на странице не больше указанного в per_page
    """
    i = 0
    r = requests.get(url, verify = False, params = params_page_get)
    x = r.json()
    count = x['per_page']
    for user in x['data']:
        i = i+1
    assert i <= count

def test_get_user_by_id_not_exist(url,params_id_get):
    """
    Проверяем, что пользователь с указанным ID не существует
    """
    i = 0
    r = requests.get(url+'/'+ str(params_id_get["id"]), verify = False)
    assert r.status_code == 404

def test_get_email_by_id(url, params_id_get):
    """
     Проверяем, что у выбранного по ID пользователь требуемая почта
     """
    r = requests.get(url + '/' + str(params_id_get["id"]), verify=False)
    x = r.json()
    assert x['data']['email'] == "eve.holt@reqres.in"

def test_post_new_user(url, params_user_post):
    """
    Добавляем нового пользователя
    """
    r = requests.post(url, data=params_user_post ,verify=False)
    assert r.status_code == 201

