"""
Provides several utility methods:

- manage.py build
  Builds the thrift files in the project
- manage.py syncdb
  Creates all registered database tables.
- manage.py dbshell
  Opens the PostgreSQL database shell.
"""

import sys
import os
from os.path import join, dirname, abspath, join, normpath
# Hack sys.path so it's callable from any folder
path = join(dirname(abspath(__file__)), "../")
sys.path.insert(0, path)

from subprocess import call
from mudserve.settings import MUDSERVE_ROOT, INSTALLED_MODELS, DATABASE
from mudserve.models import base

def main():
	args = sys.argv[1:]
	for arg in args:
		if arg in ("b", "build"):
			print "Building Thrift files...",
			cmd_build()
		elif arg == "syncdb":
			print "Synchronizing database...",
			cmd_syncdb()
		elif arg == "dbshell":
			cmd_dbshell()
		else:
			print "Argument '%s' not recognized." % arg
			continue
		print "Ok."

def cmd_build():
	gen_path = join(MUDSERVE_ROOT, "gen-py/mudserve/mudrpc/")
	mudrpc_path = join(MUDSERVE_ROOT, "mudrpc/")
	thrift_path = join(MUDSERVE_ROOT, "include.thrift")
	# Remove existing ./mudrpc folder
	call(["rm", "-rf", mudrpc_path])
	# Generate thrift files
	call(["thrift", "-r", "--gen", "py:new_style", thrift_path])
	# Move ./gen-py/mudserve/mudrpc/ to ./mudrpc/
	call(["mv", gen_path, mudrpc_path])
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

if __name__ == "__main__":
	main()
