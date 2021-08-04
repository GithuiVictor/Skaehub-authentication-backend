from main import db

class User(db.Model):
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    gender = db.Column(db.String)
    occupation = db.Column(db.String)
    address = db.Column(db.String)
    password = db.Column(db.String)
    img = db.Column(db.String)
    verify = db.Column(db.Boolean, default=False)

    #This is a nifty method which will provide a dictionary representation of the user item
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "gender": self.gender,
            "occupation": self.occupation,
            "address": self.address,
            "password": self.password,
            "img": self.img,
            "verify": self.verify
        }