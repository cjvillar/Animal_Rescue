import factory
from pytest_factoryboy import register

from animal_rescue_api.models import Animal

# builds a testing db with this animal model
@register
class AnimalFactory(factory.Factory):
    class Meta:
        model = Animal

    animal_type = (Animal.DOG,)
    name = ("x",)
    sex = ("x",)
    breed = ("x",)
    neutered = (True,)
    age = (3,)
    weight = ("x",)
    adoption_status = (Animal.AVAILABLE,)
    temperament = ("x",)
    likes = ("Playing fetch",)
    fee = ("$100",)
    location = "Shelter"
