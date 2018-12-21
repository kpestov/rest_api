from app import app
import view
from items.blueprint import items
from tree.tree_blueprint import tree
from app import db

app.register_blueprint(items, url_prefix='/classifier')
app.register_blueprint(tree, url_prefix='/tree')

if __name__ == '__main__':
    app.run()
