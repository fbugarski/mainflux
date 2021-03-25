import users
import things
import messages
import channels
import groups
import requests

channel_id = "e1eda1d2-5c08-45bf-8a79-f43e56ab77d8"
thing_id = "02dc3c7c-e33b-471d-9ab1-ba49c7c8015b"
user_id = "2803446a-4109-42e5-b07c-696e680294c8"
user = {"email": "poslednji@example.com", "password": "12345678"}
group_id = "01F1JZ23RP7VW60MKAWEF7QKG9"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTY2MjIwODMsImlhdCI6MTYxNjU4NjA4MywiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6InBvc2xlZG5qaUBleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjI4MDM0NDZhLTQxMDktNDJlNS1iMDdjLTY5NmU2ODAyOTRjOCIsInR5cGUiOjB9.xDWdnqwivjJnrSt_pNnwbIpWRfVwg8apxf_GNidgmFw"
default_url = "http://localhost"


class SDK:
    def __init__(
        self,
        users_url=default_url,
        things_url=default_url,
        messages_url=default_url,
        groups_url=default_url
    ):
        self.users = users.Users(users_url)
        self.things = things.Things(things_url)
        self.messages = messages.Messages(messages_url)
        self.channels = channels.Channels(things_url)
        self.groups = groups.Groups(groups_url)
        self.version_url = things_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()


sdk = SDK()

# '''To start working with the Mainflux system, you need to create a user account'''
# mf_resp = sdk.users.create(user)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To log in to the Mainflux system, you need to create a user token'''
# mf_resp = sdk.users.login(user)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can always check the user entity that is logged in by entering the user ID and token'''
# mf_resp = sdk.users.get(user_id, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Updating user entities in the database'''
# mf_resp = sdk.users.update(user, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get all users in the database by calling the get_all () function'''
# mf_resp = sdk.users.get_all(token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Changing the user password can be done by calling the update password function'''
# mf_resp = sdk.users.update_password("12345678", "87654321", token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To create a thing, you need the thing name and a user token'''
# mf_resp = sdk.things.create({"name": "poslednji_thing_1"}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can create multiple things at once by entering a series of things structures and a user token'''
# mf_resp = sdk.things.create_bulk([{"name": "poslednji_1", "key":""}, {"name": "poslednji_2", "key":""}, {"name": "poslednji_3", "key":""}], token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get thing information by entering the thing ID and user token'''
# mf_resp = sdk.things.get(thing_id, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get all things in the database by calling the get_all () function'''
# mf_resp = sdk.things.get_all(token, {"limit":6, "offset":5})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# mf_resp = sdk.things.get_by_channel(channel_id, {"limit":4, "offset":2}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# mf_resp = sdk.channels.get_by_thing(thing_id, {"limit":4, "offset":2}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Updating a thing entity in a database'''
# mf_resp = sdk.things.update(thing_id, token, {"key":"123456789"})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To delete a thing you need a thing ID and a user token'''
# mf_resp = sdk.things.delete("efbf85d3-7d29-464f-86b4-1de818379e7a", token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Connect thing to channel'''
# mf_resp = sdk.things.connect([channel_id], [thing_id], token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Disconnect thing from channel'''
# mf_resp = sdk.things.disconnect(channel_id, thing_id, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To create a channel, you need a channel and a token'''
# mf_resp = sdk.channels.create({"name": "poslednji_kanal_2"}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''As with things, you can create multiple channels at once'''
# mf_resp = sdk.channels.create_bulk([{"name": "poslednji_kanal2"}, {"name": "poslednji_kanal_3"}], token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Update channel entities in the database'''
# mf_resp = sdk.channels.update(channel_id, token, {"name": "poslednji_kanal_3"})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''A list of all the channels to which a given thing is connected'''
# mf_resp = sdk.channels.get_by_thing(thing_id, {}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Delete channels from the database'''
# mf_resp = sdk.channels.delete("da63c904-5d44-4b98-86fe-6aa7770c48c6", token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To create a group, you need the group name and a user token'''
# mf_resp = sdk.groups.create({"name": "poslednja_grupa_12345"}, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get group information by entering the group ID and token'''
# mf_resp = sdk.groups.get(group_id, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Group update'''
# mf_resp = sdk.groups.update(group_id, token,{})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get groups in the database by calling the get_all () function'''
# mf_resp = sdk.groups.get_all(token, group_id)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)


'''Assign'''
mf_resp = sdk.groups.assign("01F1JA2H3JDTADHHEW8DMMBA7H", token,{"members": [channel_id], "type": "channels"})
if mf_resp.error.status == 0:
    print(mf_resp.value)
else:
    print(mf_resp.error.message)

# '''Unassign'''
# mf_resp = sdk.groups.unassign("01F1JA2H3JDTADHHEW8DMMBA7H", token,{"members": [channel_id], "type": "channels"})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)


# '''Get list of members ID's from group'''
# mf_resp = sdk.groups.get(groupID, token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)
# '''proveriti'''

# '''Delete group from the database'''
# mf_resp = sdk.groups.delete("01F1J9SB5GFYC7DSB5S0R55E64", token)
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)
