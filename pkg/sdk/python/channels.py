import requests
import response
import json

class Channels:
    def __init__(self, url):
        self.url = url

    def create(self, channel, token):
        '''Creates channel entity in the database'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/channels", json=channel, headers={"Authorization": token})
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
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def create_bulk(self, channels, token):
        '''Creates multiple channels in a bulk'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/channels", json=channels, headers={"Authorization": token})
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
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def get(self, chanID, token):
        '''Gets a channel entity for a logged-in user'''
        mf_resp = response.Response()
        http_resp = requests.get(self.url + "/channels/" + chanID, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 422:
                mf_resp.error.message = "Database can't process request"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        else:
            mf_resp.value = json.loads(http_resp.json)
        return mf_resp

    def get_all(self, query_params, token):
        '''Gets all channels from database'''
        url = self.url + "/channels" + '?' + 'offset=' + query_params['offset'] + '&' + \
            'limit=' + query_params['limit'] + '&' + 'connected=' + query_params['connected']
        mf_resp = response.Response()
        http_resp = requests.get(url, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed channel's ID"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Channel does not exist"
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

    def get_by_thing(self, thingID, params, token):
        '''Gets all channels to which a specific thing is connected to'''
        query = self.construct_query(params)
        url = self.url + "/things/" + thingID + '/channels' + query
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

    def update(self, channel, token):
        '''Updates channel entity'''
        http_resp = requests.put(self.url + "/channels/" + channel["id"], json=channel, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed JSON"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 404:
                mf_resp.error.message = "Channel does not exist"
            if c == 415:
                mf_resp.error.message = "Missing or invalid content type"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp

    def delete(self, chanID, token):
        '''Deletes a channel entity from database'''
        http_resp = requests.delete(self.url + "/channels/" + chanID, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            c = http_resp.status_code
            if c == 400:
                mf_resp.error.message = "Failed due to malformed channel's ID"
            if c == 401:
                mf_resp.error.message = "Missing or invalid access token provided"
            if c == 500:
                mf_resp.error.message = "Unexpected server-side error occurred"
        return mf_resp
