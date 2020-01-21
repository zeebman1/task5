from .. import db
from sqlalchemy_utils import IPAddressType


class Location(db.Model):
    """ Location Model for storing location based on IP addr """
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ip = db.Column(IPAddressType, unique=True)
    location = db.Column(db.JSON)

    def __repr__(self):
        return "<Location for ip {}>".format(self.ip)