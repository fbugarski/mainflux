import requests


class Channels:
    def __init__(self, url):
        self.url = url

    def create(self, channel, token):
        '''Creates channel entity in the database'''
        resp = requests.post(self.url + "/channels", json=channel, headers={"Authorization": token})
        return resp.headers.get("location").split('/')[2]

    def create_bulk(self, channels, token):
        '''Creates multiple channels in a bulk'''
        resp = requests.post(self.url + "/channels", json=channels, headers={"Authorization": token})
        return resp

    def get(self, id, token):
        '''Gets a channel entity for a logged-in user'''
        resp = requests.get(self.url + "/channels/" + id, headers={"Authorization": token})
        return resp

    def get_all(self, query_params, token):
        '''Gets all channels from database'''
        url = self.url + "/channels" + '?' + 'offset=' + query_params['offset'] + '&' + \
            'limit=' + query_params['limit'] + '&' + 'connected=' + query_params['connected']
        resp = requests.get(url, headers={"Authorization": token})
        return resp.json()

    def get_by_thing(self, thing_id, query_params, token):
        '''Gets all channels to which a specific thing is connected to'''
        url = self.url + "/things/" + thing_id + '/channels' + '?' + 'offset=' + query_params['offset'] \
                + '&' + 'limit=' + query_params['limit'] + '&' + 'connected=' + query_params['connected']
        resp = requests.post(url, headers={"Authorization": token})
        return resp

    def update(self, channel, token):
        '''Updates channel entity'''
        resp= requests.put(self.url + "/channels/" + channel["id"], json=channel, headers={"Authorization": token})
        return resp

    def delete_channel(self, id, token):
        '''Deletes a channel entity from database'''
        resp = requests.delete(self.url + "/channels/" + id, headers={"Authorization": token})
        return resp
