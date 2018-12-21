from app import db
from models import TreeNode

db.create_all()

node = TreeNode(name='rootnode', body=None)
TreeNode(name='node1', parent=node, body=None)
TreeNode(name='subnode1', parent=node.children['node1'], body='some text')
subnode = TreeNode(name='my subnode2', parent=node.children['node1'], body='some text')

db.session.add(node)
db.session.commit()

print(node.dump())
print(subnode.slug)
