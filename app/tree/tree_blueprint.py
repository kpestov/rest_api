from flask import Blueprint
from flask import render_template
from models import TreeNode
from .forms import Itemform
from flask import request
from app import db
from flask import redirect, url_for


tree = Blueprint('tree', __name__, template_folder='templates')


@tree.route('/create', methods=['POST', 'GET'])
def create_item():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            item = Item(title=title, body=body)
            db.session.add(item)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('items.index'))

    form = Itemform()
    return render_template('items/create_item.html', form=form)


@tree.route('/')
def index():

    q = request.args.get('q')

    if q:
        elements = TreeNode.query.filter(TreeNode.name.contains(q) | TreeNode.body.contains(q)).all()
    else:
        elements = TreeNode.query.all()

    root = TreeNode.query.filter(TreeNode.parent_id.is_(None)).first()
    root_child = TreeNode.query.filter(TreeNode.parent_id == root.id).first()
    subnodes = TreeNode.query.filter(TreeNode.body.isnot(None)).all()

    return render_template('tree/index.html',
                           elements=elements,
                           root=root,
                           root_child=root_child,
                           subnodes=subnodes
                           )


@tree.route('/<slug>')
def subnode_detail(slug):
    subnode = TreeNode.query.filter(TreeNode.slug==slug).first()
    return render_template('tree/subnode_detail.html', subnode=subnode)

