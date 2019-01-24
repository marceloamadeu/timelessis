"""File for all models in Timeless"""

from timeless import DB

class Company(DB.Model):
    """"Model for company business entity"""
    __tablename__ = 'companies'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    def __init__(self, id):
        """Initialization method"""
        self.id = id


class Location(DB.Model):
    """"Model for location business entity"""
    __tablename__ = 'locations'

    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)

    name = DB.Column(DB.String, unique=True, nullable=False)
    code = DB.Column(DB.String, unique=True, nullable=False)
    company_id = DB.Column(DB.String, unique=True, nullable=False)
    country = DB.Column(DB.String, nullable = False)
    region = DB.Column(DB.String, nullable = False)
    city = DB.Column(DB.String, nullable = False)
    address = DB.Column(DB.String, nullable = False)
    longitude = DB.Column(DB.String, nullable = False)
    latitude = DB.Column(DB.String, nullable = False)
    type = DB.Column(DB.String, nullable = False)
    status = DB.Column(DB.String, nullable = False)
    comment = DB.Column(DB.String, nullable = True)

    def __repr__(self):
        return '<Location %r>' % self.name
