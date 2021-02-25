import requests
import response
import json


class Users:
    def __init__(self, url):
        self.url = url

    def create(self, user):
        '''Creates user entity in the database'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/users", json=user)
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 409:
                mf_resp.error.message = "Failed due to using an existing email address"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def login(self, user):
        '''Creates a user token'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/tokens", json=user)
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 409:
                mf_resp.error.message = "Failed due to using an existing email address"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = http_resp.json()["token"]
        return mf_resp

    def get(self, id, token):
        '''Gets a user entity for a logged-in user'''
        mf_resp = response.Response()
        http_resp = requests.get(self.url + "/users/" + id, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed query parameters"
            if c == 403:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def get_all(self, token):
        '''Gets all users from database'''
        http_resp = requests.get(self.url + "/users", headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed query parameters"
            if c == 403:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, user, token):
        '''Updates user entity'''
        http_resp = requests.put(self.url + "/users", headers={"Authorization": token}, data=json.dumps(user))
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 403:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Failed due to non existing user"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp

    def update_password(self, old_password, new_password, token):
        '''Changes user password'''
        payload = {
          "old_password": old_password,
          "new_password": new_password
        }
        http_resp = requests.patch(self.url + "/password", headers={"Authorization": token}, data=json.dumps(payload))
        mf_resp = response.Response()
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp
