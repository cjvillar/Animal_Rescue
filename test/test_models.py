import pytest

from animal_rescue_api.models import Animal

from .factories import AnimalFactory

pytestmark = pytest.mark.django_db


class TestAnimalModel:
    def test_animal_creation(self, animal_factory):
        animal = animal_factory(
            animal_type="Dog",
            name="Fido",
            sex="Male",
            breed="Labrador",
            neutered=True,
            age=3,
            weight="20kg",
            adoption_status="AVAILABLE",
            temperament="Friendly",
            likes="Playing fetch",
            fee="$100",
            location="Shelter",
        )

        # assert attributes of animal
        assert animal.animal_type == "Dog"
        assert animal.name == "Fido"
        assert animal.sex == "Male"
        assert animal.breed == "Labrador"
        assert animal.neutered is True
        assert animal.age == 3
        assert animal.weight == "20kg"
        assert animal.adoption_status == "AVAILABLE"
        assert animal.temperament == "Friendly"
        assert animal.likes == "Playing fetch"
        assert animal.fee == "$100"
        assert animal.location == "Shelter"
