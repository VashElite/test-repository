from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    time = db.Column(db.String(80))
    status = db.Column(db.Integer())
    check = db.Column(db.Integer())
    tip = db.Column(db.Integer())
    total =  db.Column(db.Integer())
    btc_asks = db.Column(db.Integer())
    btc_convert = db.Column(db.Float(precision=7))
    btc_raccount = db.Column(db.String(80))
    commission = db.Column(db.Float(precision=7))
 
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, time, status, check, tip, 
                total, btc_asks, btc_convert, btc_raccount,
                 commission, store_id):
        self.name = name
        self.time = time
        self.status = status
        self.check = check
        self.tip = tip
        self.total =  total
        self.btc_asks = btc_asks
        self.btc_convert = btc_convert
        self.btc_raccount = btc_raccount
        self.commission = commission
        self.store_id = store_id
        

    def json(self):
        return {'name': self.name, 'time':  self.time, 'status': self.status, 
                'check': self.check, 'tip': self.tip, 'total':  self.total, 
                'btc_asks': self.btc_asks, 'btc_convert': self.btc_convert,
                'btc_raccount': self.btc_raccount, 'commission': self.commission}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
