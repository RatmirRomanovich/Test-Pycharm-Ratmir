import pytest
import requests


def test_post_positive():

    url = "https://petstore.swagger.io/v2/pet"
    request = {}

    request['name'] = 'abuzer'

    request['category'] = {}
    request['category']['name'] = 'dog'

    request['photoUrls'] = ['photochki']

    print("request = ", request)

    response = requests.post(url, json=request)

    print("request = ", response.json())

    assert response.json()["id"] is not None
    assert response.json()["name"] == request['name']

    urlGet = "https://petstore.swagger.io/v2/pet/" + str(response.json()['id'])
    print('urlGet = ', urlGet)
    responseGet = requests.get(urlGet)
    print("response Get = ", responseGet.json())

    assert responseGet.json()['id'] == response.json()['id']
    assert responseGet.json()['name'] == request['name']

def test_post_negative():

    url = "https://petstore.swagger.io/v2/pet"
    request = {}

    request['name'] = []

    request['category'] = {}
    request['category']['name'] = 'dog'

    request['photoUrls'] = ['photochki']

    print("request = ", request)

    response = requests.post(url, json=request)

    print("request = ", response.json())

    assert response.json()['message'] == 'something bad happened'



def test_get_id():

    url = "https://petstore.swagger.io/v2/pet/1"
    response = requests.get(url)
    print("response = ", response.json())
    assert response.json()["id"] == 1

def test_get_negative_id():
    url = "https://petstore.swagger.io/v2/pet/9994545756756"
    response = requests.get(url)
    print("response = ", response.json())
    assert response.json()["message"] == "Pet not found"