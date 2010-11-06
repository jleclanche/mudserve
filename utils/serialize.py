#!/usr/bin/env python

def update(db, objects):
	serialize = Serializer()
	file = db.file
	data = serialize.from_file(db, file)
	for obj in objects:
		# XXX check ids?
		data.objects.append(obj)
	
	serialize.to_file(db, file, data)

argtable = ( # i dont have braces.
	"spell": SpellDatabase,
	"map": MapDatabase,
)

def main():
	import sys
	args = sys.argv[1:]
	databases = []
	for arg in set(args):
		if arg in argtable:
			databases.append(argtable[arg])
	
	for db in databases:
		objects = [] # get them from where?
		update(db, objects)

if __name__ == "__main__":
	main()