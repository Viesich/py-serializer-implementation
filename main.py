import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data).encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode("utf-8")
    data = json.loads(json_str)

    serializer = CarSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        car_instance = serializer.save()
        return car_instance
