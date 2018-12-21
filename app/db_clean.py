from models import TreeNode
from app import db
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqlconnector://root:Ft28021-28081991@localhost/test1')
TreeNode.__table__.drop(engine)
db.session.commit()