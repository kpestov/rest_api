from flask import Blueprint
from flask import render_template
from models import TreeNode


tree = Blueprint('tree', __name__, template_folder='templates')


@tree.route('/')
def index():
    items = TreeNode.query.all()
    root = TreeNode.query.filter(TreeNode.parent_id.is_(None)).first()
    root_child = TreeNode.query.filter(TreeNode.parent_id == root.id).first()
    subnodes = TreeNode.query.filter(TreeNode.body.isnot(None)).all()
    return render_template('tree/index.html',
                           items=items,
                           root=root,
                           root_child=root_child,
                           subnodes=subnodes
                           )


@tree.route('/<slug>')
def subnode_detail(slug):
    subnode = TreeNode.query.filter(TreeNode.slug==slug).first()
    return render_template('tree/subnode_detail.html', subnode=subnode)

