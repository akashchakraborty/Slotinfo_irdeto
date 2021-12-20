from slotinfo import db
from datetime import*

class Item(db.Model):
        slotID = db.Column(db.String(length=10),primary_key=True)
        rack_number = db.Column(db.Integer(), nullable=False)
        slot_number = db.Column(db.Integer(), nullable=False)
        days_taken = db.Column(db.Integer(),nullable=False)
        project = db.Column(db.String(length=30),nullable=False)
        name = db.Column(db.String(length=50),nullable=False)
        description = db.Column(db.String(length=1024),nullable=True)
        
        def __repr__(self):
            return f'Item {self.slotID}'

### dummy class ###

## error solved by pooh! ##