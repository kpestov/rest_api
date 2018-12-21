from flask import Blueprint
from flask import render_template
from models import Item, Tag



items = Blueprint('items', __name__, template_folder='templates')


@items.route('/')
def index():
    items = Item.query.all()
    return render_template('items/index.html', items=items)


@items.route('/<slug>')
def item_details(slug):
    item = Item.query.filter(Item.slug==slug).first()
    tags = item.tags
    return render_template('items/item_detail.html', item=item, tags=tags)


@items.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    items = tag.items.all()
    return render_template('items/tag_detail.html', tag=tag, items=items)


