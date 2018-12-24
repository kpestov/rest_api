from app import app
import view
from tree.tree_blueprint import tree
from app import db
# from api.server import api

app.register_blueprint(tree, url_prefix='/tree')


if __name__ == '__main__':
    app.run()
    # api.run(host='0.0.0.0', port=8000, debug=True)

