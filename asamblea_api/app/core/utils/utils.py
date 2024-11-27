import uuid


def validate_geolocation(lat: float, lon: float) -> bool:
    return -90 <= lat <= 90 and -180 <= lon <= 180


def generate_unique_id():
    return str(uuid.uuid4())
