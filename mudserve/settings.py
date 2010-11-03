from os.path import join, dirname, abspath

# The path to the mudserve root relative to the current working directory.
MUDSERVE_ROOT = abspath(dirname(__file__))
DATA_ROOT = join(MUDSERVE_ROOT, "data/")

# The database configuration
DATABASE = {
	"type": "postgresql",
	"username": "ctmud",
	"password": "sR89fl1GhM5",
	"hostname": "",
	"database": "mudserve",
	"port": 5432
}

# Installed database models
INSTALLED_MODELS = (
	"mudserve.models.user",
)
