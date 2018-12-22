from app import app
import view
from tree.tree_blueprint import tree
from app import db




app.register_blueprint(tree, url_prefix='/tree')


if __name__ == '__main__':
    app.run()

