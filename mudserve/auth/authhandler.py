from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
from time import time as utctime
from cPickle import loads, dumps
from base64 import encodestring, decodestring
from hashlib import md5
from mudserve.settings import SECRET_KEY
from mudserve.mudrpc.auth.types.ttypes import User, MUDAUserException, MUDAErrorCode
from mudserve.models.auth import Auth
from mudserve import cache
from mudserve import dbsession

class AuthHandler(object):
	def validate_token(self, auth_token):
		# Decode token
		user_id = cache.get(auth_token, namespace="auth")
		if user_id is None:
			# Check database
			try:
				auth = dbsession.query(Auth).filter(Auth.auth_token == auth_token,
				  Auth.expire_time<datetime.utcnow()).one()
			except NoResultFound:
				# The auth has expired
				raise MUDAUserException(errorCode=MUDAErrorCode.AUTH_EXPIRED)
			# Auth token valid, cache the result
			user_id = auth.user_id
			cache.set(auth_token, user_id, namespace="auth")
		return user_id

def _generate_auth_token(user_id):
	data = (userId, utctime())
	pickled_data = dumps(data)
	pickled_md5 = md5(pickled_data + SECRET_KEY).hexdigest()
	return encodestring(pickled + pickled_md5)
	
