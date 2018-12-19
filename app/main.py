from app import app
import view
from items.blueprint import items
from app import db

app.register_blueprint(items, url_prefix='/classifier')

if __name__ == '__main__':
    app.run()
