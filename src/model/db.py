from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import uuid
import os


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean, default=False)


def create_user(username, password, admin=False):
    if User.query.filter_by(name=username).first():
        return

    default_user = User(public_id=str(uuid.uuid4()),
                        name=username,
                        password=generate_password_hash(password, method='sha256'),
                        admin=admin)
    db.session.add(default_user)
    db.session.commit()


def create_db(app, create_default_user):
    app.app_context().push()
    db.create_all()

    if create_default_user:
        create_user(os.getenv("DEFAULT_USER"), os.getenv("DEFAULT_PASSWORD"))
