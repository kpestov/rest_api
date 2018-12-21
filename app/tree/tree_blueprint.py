from flask import Blueprint
from flask import render_template
from models import TreeNode
from .forms import ItemForm
from flask import request
from app import db
from flask import redirect, url_for


tree = Blueprint('tree', __name__, template_folder='templates')


@tree.route('/create', methods=['POST', 'GET'])
def create_item():

    parent_node = TreeNode.query.filter(TreeNode.parent_id == 1).first()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            item = TreeNode(name=title, parent=parent_node, body=body)
            db.session.add(item)
            db.session.commit()
        except:
            print('Something wrong')

        return redirect(url_for('tree.index'))

    form = ItemForm()
    return render_template('tree/create_item.html', form=form)


@tree.route('/<slug>/edit/', methods=['POST', 'GET'])
def edit_item(slug):
    element = TreeNode.query.filter(TreeNode.slug == slug).first()

    if request.method == 'POST':
        form = ItemForm(formdata=request.form, obj=element)
        # tree.name = request.form['title']
        # tree.name = request.form['body']
        form.populate_obj(element)
        db.session.commit()

        return redirect(url_for('tree.subnode_detail', slug=element.slug))

    form = ItemForm(obj=element)
    return render_template('tree/edit_item.html', element=element, form=form)


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

