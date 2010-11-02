from time import time as utctime
from mudserve.mudrpc.auth_types.ttypes import User

class AuthHandler(object):
	def validate_token(self, authToken):
		# Raise exception if invalid here
		# TODO: Return proper info from database here
		user = User(id=1, username="FIXME", active=True, created=utctime())
		return user
