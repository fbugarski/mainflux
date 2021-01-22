import request
import json

def CreateChannel(channel, token):
    resp = requests.post("http://localhost/channels", json=channel, headers={"Authorization": token})
    return resp.headers.get("location")

def CreateChannels(channels, token):
    resp = requests.post("http://localhost/channels", json=channels, headers={"Authorization": token})
    return resp

def Channels(params, token):
    url = "http://localhost/channels"+'?'+'offset='+params['offset']+'&'+'limit='+params['limit']+'&'+'connected='+params['connected']
    resp = requests.get(url, headers={"Authorization": token})
    return resp.json()

def ChannelsByThing(thingID, params, token):
    url = "http://localhost/things"+thingID+'/channels'+'?'+'offset='+params['offset']+'&'+'limit='+params['limit']+'&'+'connected='+params['connected']
    resp = requests.post(url, json=channels, headers={"Authorization": token})
    return resp

def Channel(id, token):
    resp = requests.get("http://localhost/channels/"+id, headers={"Authorization": token})
    return resp

def UpdateChannel(channel, token):
    resp= requests.put("http://localhost/channels/"+channel["id"], json=channel, headers={"Authorization": token}) 
    return resp

def DeleteChannel(id, token):
    resp = requests.delete("http://localhost/channels/"+id, headers={"Authorization": token})
    return resp
