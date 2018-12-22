from app import db
from models import TreeNode

db.create_all()

node = TreeNode(name='Programming language', body=None)
TreeNode(name='Dynamically typed languages', parent=node, body=None)
TreeNode(name='Python', parent=node.children['Dynamically typed languages'], body='some text')
subnode = TreeNode(name='JavaScript', parent=node.children['Dynamically typed languages'], body='some text')

db.session.add(node)
db.session.commit()

print(node.dump())
