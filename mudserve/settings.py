from os.path import join, dirname, abspath

# The absolute path to the mudserve root.
MUDSERVE_ROOT = abspath(dirname(__file__))

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

SECRET_KEY = "11f458a541f44dcf8752c84d16ac8858"
