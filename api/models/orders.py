from ..utils import db
from enum import Enum
from datetime import datetime

class Sizes(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large' 
    EXTRA_LARGE = 'extra_large'

class OrderStatus(Enum):
    PENDING = 'pending'
    IN_TRANSIT = 'in_transit'
    DELIVERED = 'delivered'

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer(), primary_key=True)
    size = db.Column(db.Enum(Sizes), default=Sizes.MEDIUM)
    order_status = db.Column(db.Enum(OrderStatus), default=OrderStatus.IN_TRANSIT)
    flavor = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer(), default=1)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    customer = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __repr__(self):
         return f"<User{self.id}>"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_by_id(cls,id):
        return cls.query.get_or_404(id)


    def delete(self):
        db.session.delete(self)
        db.session.commit()