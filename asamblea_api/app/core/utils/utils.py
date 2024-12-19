import uuid


# Validate geolocation coordinates input
def validate_geolocation(lat: float, lon: float) -> bool:
    return -90 <= lat <= 90 and -180 <= lon <= 180


# Generate UUID v4 like a string
def generate_unique_id():
    return str(uuid.uuid4())
