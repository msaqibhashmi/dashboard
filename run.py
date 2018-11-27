from webapp import app, db
from webapp.models import User


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
