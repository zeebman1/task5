import unittest
from app.main import db
from app.main.model.location import Location
from app.test.base import BaseTestCase


class TestLocation(BaseTestCase):

    def test_encode_auth_token(self):
        ip = '153.239.251.234'
        location = Location(
            ip=ip,
            location={'ip': ip, 'type': None, 'continent_code': None, 'continent_name': None, 'country_code': None, 'country_name': None, 'region_code': None, 'region_name': None, 'city': None, 'zip': None, 'latitude': None, 'longitude': None, 'location': {'geoname_id': None, 'capital': None, 'languages': None, 'country_flag': None, 'country_flag_emoji': None, 'country_flag_emoji_unicode': None, 'calling_code': None, 'is_eu': None}},
        )
        db.session.add(location)
        db.session.commit()
        location = Location.query.filter_by(id=location.id).first()
        self.assertFalse(location is None)


if __name__ == '__main__':
    unittest.main()

