import requests
import json

import response
import errors


class Groups:
    def __init__(self, url):
        self.url = url

    def create(self, group, token):
        '''Creates group entity in the database'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/groups", json=group, headers={"Authorization": token})
        if http_resp.status_code != 201:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["create"], http_resp.status_code)
        else:
            location = http_resp.headers.get("location")
            mf_resp.value = location.split('/')[2]
        return mf_resp

    def get(self, group_id, token):
        '''Gets a group entity'''
        mf_resp = response.Response()
        http_resp = requests.get(self.url + "/groups/" + group_id, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["get"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def construct_query(self, params):
        query = '?'
        param_types = ['offset', 'limit', 'connected']
        if params is not None:
            for pt in param_types:
                if params[pt] is not None:
                    query = query + pt + params[pt] + '&'
        return query

    def get_all(self, token, query_params=None):
        '''Gets all things from database'''
        query = self.construct_query(query_params)
        url = self.url + '/groups' + query
        mf_resp = response.Response()
        http_resp = requests.get(url, headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["get_all"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def update(self, group_id, token, group):
        '''Updates group entity'''
        http_resp = requests.put(self.url + "/groups/" + group_id, json=group, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["update"], http_resp.status_code)
        return mf_resp

    def members(self, group_id, token):
        '''Get list of members ID's from group'''
        http_resp = requests.post(self.url + "/groups/" + group_id + "/members", headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["members"], http_resp.status_code)
        return mf_resp

    def assign(self, group_id, token, group):
        '''Assign'''
        mf_resp = response.Response()
        http_resp = requests.post(self.url + "/groups/" + group_id + "/members", headers={"Authorization": token}, json=group)
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["assign"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def unassign(self, group_id, id, token):
        '''Assign'''
        mf_resp = response.Response()
        http_resp = requests.delete(self.url + "/groups/" + group_id + "/members", headers={"Authorization": token})
        if http_resp.status_code != 200:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["unassign"], http_resp.status_code)
        else:
            mf_resp.value = http_resp.json()
        return mf_resp

    def delete(self, group_id, token):
        '''Deletes a group entity from database'''
        http_resp = requests.delete(self.url + "/groups/" + group_id, headers={"Authorization": token})
        mf_resp = response.Response()
        if http_resp.status_code != 204:
            mf_resp.error.status = 1
            mf_resp.error.message = errors.handle_error(errors.users["delete"], http_resp.status_code)
        return mf_resp
