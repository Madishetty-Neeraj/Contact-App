from contacts import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    secret=db.Column(db.String(10),nullable=False)
    contact=db.relationship('Contact',backref='author',lazy=True)
    def __repr__(self):
        return f"User('{self.id},{self.username},{self.email},{self.password}')"


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pnumber = db.Column(db.String(10),unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Contact('{self.id},{self.name},{self.email},{self.pnumber}')"