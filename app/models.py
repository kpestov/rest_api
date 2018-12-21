from app import db
import re
from sqlalchemy.orm.collections import attribute_mapped_collection


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


item_tags = db.Table('item_tags',
                     db.Column('item_id', db.Integer, db.ForeignKey('item.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                     extend_existing=True
                     )


class TreeNode(db.Model):
    __tablename__ = 'tree'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey(id) )
    name = db.Column(db.String(50), nullable=False)
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


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=item_tags, backref=db.backref('items', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Item id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id, self.name)
