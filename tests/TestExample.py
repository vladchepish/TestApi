from api import random


class TestExample:

    def test_create_new_booking(self, client):
        data = random.random_booking()
        res = client.vr(client.create_booking(data), [200, 201])
        created = res.json()
        assert created.get("bookingid")
        assert created.get("booking") == data
