import requests
import response
import json

class Things:
    def __init__(self, url):
        self.url = url

    def create(self, thing, token):
        '''Creates thing entity in the database'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/things", json=thing, headers={"Authorization": token})
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 409:
                mf_resp.error.message = "Entity already exist"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 422:
                mf_resp.error.message = "Database can't process request"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def create_bulk(self, things, token):
        '''Creates multiple things in a bulk'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/things", json=things, headers={"Authorization": token})
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 409:
                mf_resp.error.message = "Entity already exist"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 422:
                mf_resp.error.message = "Database can't process request"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def get(self, id, token):
        '''Gets a thing entity for a logged-in user'''
        mf_resp = response.Response()
        http_resp = requests.get(self.url + "/things/" + id, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Thing does not exist"
            if c == 422:
                mf_resp.error.message = "Database can't process request"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp

    def get_all(self, params, token):
        '''Gets all things from database'''
        url = self.url + "/things" + '?' + 'offset=' + params['offset'] + '&' \
            + 'limit=' + params['limit'] + '&'+'name=' + params['name']
        mf_resp = response.Response()
        http_resp = requests.get(url, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Thing does not exist"
            if c == 422:
                mf_resp.error.message = "Database can't process request"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp

    def construct_query(self, params):
        query = '?'
        param_types = ['offset', 'limit', 'connected']
        for pt in param_types:
            if params[pt] is not None:
                query = query + pt + params[pt] + '&'
        return query

    def get_by_channel(self, id, params, token):
        '''Gets all things to which a specific thing is connected to'''
        query = self.construct_query(params)
        url = self.url + "/channels/" + id + '/things' + query
        mf_resp = response.Response()
        http_resp = requests.post(url, headers={"Authorization": token})
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 409:
                mf_resp.error.message = "Entity already exist"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp

    def update(self, thing, token):
        '''Updates thing entity'''
        http_resp = requests.put(self.url + "/things/" + thing["id"], json=thing, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Thing does not exist"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp

    def delete(self, id, token):
        '''Deletes a thing entity from database'''
        http_resp = requests.delete(self.url + "/things/" + id, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed thing's ID"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp
