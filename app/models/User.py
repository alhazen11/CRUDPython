from app import db, ma
from flask import jsonify
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'parent_id', 'name','email','password','notification', 'auto_ml', 'city', 'created_at', 'updated_at')
        ordered = True

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, default=0)
    name = db.Column(db.String(120), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    notification = db.Column(db.Boolean, default=True)
    auto_ml = db.Column(db.Boolean, default=True)
    city = db.Column(db.String(255))
    photo = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    devices = db.relationship('Device', backref='user', lazy='dynamic')
    notifications = db.relationship('Notification', backref='user', lazy='dynamic')

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    @classmethod
    def return_all(cls):
        users_schema = UserSchema(many=True)

        users = User.query.all()
        if users:
            return users_schema.jsonify(users)
        else:
            return {'message': 'Table user is empty'}, 404

    @classmethod
    def find_by_id(cls, id):
        user_schema = UserSchema()

        user = User.query.get(id)
        if user:
            return user_schema.jsonify(user)
        else:
            return {'message': 'User not found'}, 404

    @classmethod
    def delete(cls, id):
        try:
            user = cls.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User with id #{} deleted'.format(id)}
        except:
            return {'message': 'Something went wrong'}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update(id, parent_id, name, email, password, notification, auto_ml, city):
        update = User.query.get(id)
        if update:
            if not parent_id:
                update.parent_id = update.parent_id
            else:
                update.parent_id = parent_id
            if not name:
                update.name = update.name
            else:
                update.name = name
            if not email:
                update.email = update.email
            else:
                update.email = email
            if not password:
                update.password = update.password
            else:
                update.password = password
            if not notification:
                update.notification = update.notification
            else:
                update.notification = bool(notification)
            if not auto_ml:
                update.auto_ml = update.auto_ml
            else:
                update.auto_ml = bool(auto_ml)
            if not city:
                update.city = update.city
            else:
                update.city = city
            db.session.add(update)
            db.session.commit()
            return {
                'message': 'User with id #{} updated'.format(id),
                'name': update.name
            }
        else:
            return {'message': 'User not found'}, 404

    def __repr__(self):
        return '<User {}>'.format(self.name)