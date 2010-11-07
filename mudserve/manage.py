#!/usr/bin/env python
"""
Provides several utility methods:

- manage.py build
  Builds the thrift files in the project
- manage.py syncdb
  Creates all registered database tables.
- manage.py dbshell
  Opens the PostgreSQL database shell.
- manage.py serialize <database>
  Serializes the Thrift database <database> to disk.
"""

import sys
import os
from os.path import join, dirname, abspath, join, normpath
from simplejson import loads
from subprocess import call
from mudserve.settings import MUDSERVE_ROOT, INSTALLED_MODELS, DATABASE
from mudserve.models import base
from mudserve.data.databases import database_map

def main():
	if len(sys.argv) < 2:
		print "manage.py requires an action. See help(manage)."
		return
	arg = sys.argv[1]
	if arg in ("b", "build"):
		print "Building Thrift files...",
		cmd_build()
	elif arg in ("s", "serialize"):
		cmd_serialize(args[2:])
	elif arg == "syncdb":
		print "Synchronizing database...",
		cmd_syncdb()
	elif arg == "dbshell":
		cmd_dbshell()
	else:
		print "Argument %r not recognized." % (arg)
		return
	print "Ok."

def cmd_build():
	gen_path = abspath(join(MUDSERVE_ROOT, "gen-py/"))
	gen_rpc_path = join(gen_path, "mudserve/mudrpc/")
	mudrpc_path = abspath(join(MUDSERVE_ROOT, "mudrpc/"))
	thrift_path = abspath(join(MUDSERVE_ROOT, "include.thrift"))
	# Remove existing ./mudrpc folder
	call(["rm", "-rf", mudrpc_path])
	# Generate thrift files
	call(["thrift", "-r", "--gen", "py:new_style", thrift_path])
	# Move ./gen-py/mudserve/mudrpc/ to ./mudrpc/
	call(["mv", gen_rpc_path, mudrpc_path])
	# Remove generated folder that is now empty
	call(["rm", "-rf", gen_path])

def cmd_syncdb():
	for app in INSTALLED_MODELS:
		try:
			__import__(app)
		except ImportError:
			print "Could not import module '%s'. Aborting." % app
			break
	base.Base.metadata.create_all(base.engine)

def cmd_dbshell():
	args = ["psql"]
	if DATABASE["username"]:
		args += ["-U", DATABASE["username"]]
	if DATABASE["hostname"]:
		args += ["-h", DATABASE["hostname"]]
	if DATABASE["port"]:
		args += ["-p", str(DATABASE["port"])]
	args += [DATABASE["database"]]
	if os.name == "nt":
		sys.exit(os.system(" ".join(args)))
	else:
		os.execvp(args[0], args)

def cmd_serialize(args):
	for arg in set(args):
		if arg in database_map:
			db = database_map[arg]
			# Grab the objects
			json_path = db.get_json_path()
			f = open(json_path, "r")
			data = loads(f.read())
			f.close()
			print data
			continue
			# Create the database instance
			obj = db.DATABASE_STRUCT(objects=data)
			# Serialize it to file
			db.save_database(obj)
if __name__ == "__main__":
	main()
