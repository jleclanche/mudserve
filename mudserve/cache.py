import memcache

MEMCACHED_HOST = "127.0.0.1:11211"

cache = memcache.Client([MEMCACHED_HOST], debug=0)
