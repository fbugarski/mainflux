import users
import things
import messages
import channels
import requests


default_url = "http://localhost"


class SDK:
    def __init__(
        self,
        users_url=default_url,
        things_url=default_url,
        messages_url=default_url
    ):
        self.users = users.Users(users_url)
        self.things = things.Things(things_url)
        self.messages = messages.Messages(messages_url)
        self.channels = channels.Channels(things_url)
        self.version_url = things_url

    def version(self):
        response = requests.get(self.version_url + "/version")
        return response.json()


sdk = SDK()

# '''To start working with the Mainflux system, you need to create a user account'''
# mf_resp = sdk.users.create({"email": "darkic1@example.com", "password": "12345678"})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To log in to the Mainflux system, you need to create a user token'''
# mf_resp = sdk.users.login({"email": "darkic@example.com", "password": "12345678"})
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can always check the user entity that is logged in by entering the user ID and token'''
# mf_resp = sdk.users.get('ece6161c-acdf-47ef-a5f1-ccafe9cd661e', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I')
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Updating user entities in the database'''
# mf_resp = sdk.users.update({"email": "darkic1@example.com", "password": "12345678"}, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I')
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can get a request for all users in the database by calling the get_all () function'''
# mf_resp = sdk.users.get_all('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I')
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Changing the user password can be done by calling the update password function'''
# mf_resp = sdk.users.update_password("12345678", "123456789", 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I')
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To create a thing, you need the thing name and a user token'''
# mf_resp = sdk.things.create({"name": "connect"}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3ODA3ODMsImlhdCI6MTYxMzc0NDc4MywiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.CArffZ1FYPtIT3VUJbzFS-2CZDvwmC0cw3xBNeyNm_8")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''You can create multiple things at once by entering a series of things structures and a user token'''
# mf_resp = sdk.things.create_bulk({"things": [{"name": "pera"},{"name": "mika"}]}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)
# '''proveriti'''

# '''You can get thing information by entering the thing ID and user token'''
# mf_resp = sdk.things.get("e813ebf1-f218-441d-a4f1-d9f9937c4946", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Updating a thing entity in a database'''
# mf_resp = sdk.things.update({"id": "e813ebf1-f218-441d-a4f1-d9f9937c4946", "name": "flp1"}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To delete a thing you need a thing ID and a user token'''
# mf_resp = sdk.things.delete("e813ebf1-f218-441d-a4f1-d9f9937c4946", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Connect the thing to the channel'''
# mf_resp = sdk.things.connect("7a8bd64a-8af7-4122-9c45-7550382c09a5", "7f6904cb-8465-4d74-b01e-ab7e2cdad115", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3ODA3ODMsImlhdCI6MTYxMzc0NDc4MywiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.CArffZ1FYPtIT3VUJbzFS-2CZDvwmC0cw3xBNeyNm_8")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Disconnect the thing form the channel'''
# mf_resp = sdk.things.delete("e813ebf1-f218-441d-a4f1-d9f9937c4946", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3MTkxNjgsImlhdCI6MTYxMzY4MzE2OCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.Eoc6RDMimJh9W3wI4RHragoTvDk5XcbQn_3FzpevW7I")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''To create a channel, you need a channel and a token'''
# mf_resp = sdk.channels.create({"flp": "filipina"}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTM3ODA3ODMsImlhdCI6MTYxMzc0NDc4MywiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6ImRhcmtpY0BleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6IjhiMjExMGQxLTVmMTktNDZkYS1hMzQ1LTA1ZTc2OGY2ZGQzYSIsInR5cGUiOjB9.CArffZ1FYPtIT3VUJbzFS-2CZDvwmC0cw3xBNeyNm_8")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''As with things, you can create multiple channels at once'''
# mf_resp = sdk.channels.create_bulk({"name": ["pfc", "pfc1"]}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTI4MzA2NzEsImlhdCI6MTYxMjc5NDY3MSwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6InRlc3QxMjM0NTY3OEBleGFtcGxlLmNvbSIsImlzc3Vlcl9pZCI6ImNmZTQ1MDJkLTRlOTEtNDliYS04NjRkLTA1ZDM3OWM2NWMzZCIsInR5cGUiOjB9._tBOrgfQ_cG5RssztwBywXrgXXzNjPlT4PhCWYkkysI")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Update channel entities in the database'''
# mf_resp = sdk.channels.update("channel ID", "token")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''A list of all the channels to which a given thing is connected'''
# mf_resp = sdk.things.get_by_channel("736c8396-7cda-45ec-a43a-aac05e7af9d1", {"offset": "10", "limit": "10", "connected": "10"}, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTMwMDY2ODAsImlhdCI6MTYxMjk3MDY4MCwiaXNzIjoibWFpbmZsdXguYXV0aCIsInN1YiI6InRlc3RpYzFAZXhhbXBsZS5jb20iLCJpc3N1ZXJfaWQiOiIxOTQ0NjU5Zi00ZWJhLTQ2ZGItOWRkZC02MjMwNjkxOWY4YWYiLCJ0eXBlIjowfQ.np45yUtgd50MH2hWlKAuNkhLw-L7vzTa3TEl-sYfkOM")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)

# '''Delete channels from the database'''
# mf_resp = sdk.things.delete("channel ID", "token")
# if mf_resp.error.status == 0:
#     print(mf_resp.value)
# else:
#     print(mf_resp.error.message)
