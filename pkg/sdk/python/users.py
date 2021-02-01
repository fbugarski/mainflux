import requests
import json


class Users:
    def __init__(self, url):
        self.url = url

    def create(self, user):
        '''Creates user entity in the database'''
        resp = requests.post(self.url + "/users", json=user)
        return resp.headers.get("location").split('/')[2]

    def get_all(self, token):
        '''Gets all users from database'''
        resp = requests.get(self.url + "/users", headers={"Authorization": token})
        return resp.content

    def get(self, id, token):
        '''Gets a user entity for a logged-in user'''
        resp = requests.get(self.url + "/users/" + id, headers={"Authorization": token})
        return resp.content

    def login(self, user):
        '''Creates a user token'''
        resp = requests.post(self.url + "/tokens", json=user)
        return resp.json()["token"]

    def update(self, user, token):
        '''Updates user entity'''
        resp = requests.put(self.url + "/users", headers={"Authorization": token}, data=json.dumps(user))
        return resp.status_code

    def update_password(self, old_password, new_password, token):
        '''Changes user password'''
        payload = {
          "old_password": old_password,
          "new_password": new_password
        }
        resp = requests.patch(self.url + "/password", headers={"Authorization": token}, data=json.dumps(payload))
        return resp
