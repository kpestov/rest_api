import re
from sqlalchemy.orm.collections import attribute_mapped_collection

# from app import db

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy(app)


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class TreeNode(db.Model):
    __tablename__ = 'tree'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey(id) )
    name = db.Column(db.String(50), nullable=False, unique=True)
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)

    children = db.relationship(
        "TreeNode",
        cascade='all, delete-orphan',
        backref=db.backref('parent', remote_side=id),
        collection_class=attribute_mapped_collection('name')
    )

    def __init__(self, parent=None, *args, **kwargs):
        super(TreeNode, self).__init__(*args, **kwargs)
        self.generate_slug()
        self.parent = parent


    def generate_slug(self):
        if self.body:
            self.slug = slugify(self.name)

    def __repr__(self):
        return 'TreeNode(name: {}, id: {}, parent_id: {}, body: {})'.format(self.name, self.id, self.parent_id, self.body)

    def dump(self, _indent=0):
        return '   ' * _indent + repr(self) + '\n' + ''.join([c.dump(_indent + 1) for c in self.children.values()])