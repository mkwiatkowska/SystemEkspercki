from flaskblog import db
# from flask import current_app
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from datetime import datetime
# from flask_login import UserMixin


class PerfumeInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    top = db.Column(db.String(100), nullable=False)
    heart = db.Column(db.String(100), nullable=False)
    base = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    #p_scent = db.relationship('PerfumeScents', backref='perfume scent pi', lazy=True)
    # p_preference = db.relationship(
    #     'UserPreferences', backref='perfume preference', lazy=True)

    def __repr__(self):
        return f"({self.id},{self.name},{self.brand})"

    def get_info(self):
        return (self.id, self.name, self.brand)

    def get_type(self):
        return self.group


class Scents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    group = db.Column(db.String(50), nullable=False)
    #prefume_scent = db.relationship('PerfumeScents', backref='perfume scent s', lazy=True)

    def __repr__(self):
        return f"({self.id},{self.name})"

    def get_info(self):
        return (self.id, self.name)

# class UserPreferences(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     perfume_id = db.Column(db.Integer, db.ForeignKey(
#         'perfume_info.id'), nullable=False)

#     def __repr__(self):
#         return f"({self.id}, {self.perfume_id})"


# class MyPreferences(db.Model):
#     perfume_id = db.Column(db.Integer, db.ForeignKey(
#         'perfume_info.id'), nullable=False)

#     def __repr__(self):
#         return f"({self.perfume_id})"
