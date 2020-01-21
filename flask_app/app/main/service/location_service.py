import requests
from app.main.model.location import Location
from app.main.util.db_util import save_changes

key = 'a544aecdde85a1f52a56292f77ecde6e'


def save_location(ip_addr):
    try:
        location_data = get_location(ip_addr=ip_addr)
        location = Location(
            ip=ip_addr,
            location=location_data
        )
        save_changes(location)

    except Exception as e:
        if 'UNIQUE constraint failed: location.ip' not in str(e):
            response_object = {
                'status': 'fail',
                'message': e
            }
            return response_object, 400

    response_object = {
        'status': 'success',
        'message': 'Successfully saved location.',
        'location': location_data
    }
    return response_object, 200

def get_location(ip_addr):
    r = requests.get('http://api.ipstack.com/{ip}?access_key={key}'.format(ip=ip_addr, key=key))
    return r.text