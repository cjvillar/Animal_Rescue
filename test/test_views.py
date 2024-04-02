import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from animal_rescue_api.models import Animal


@pytest.fixture
def created_animal():
    client = APIClient()
    url = reverse("animal-list-create")
    data = {
        "animal_type": "Dog",
        "name": "test_dog",
        "sex": "Male",
        "breed": "Labrador",
        "neutered": True,
        "age": 3,
        "weight": "20kg",
        "adoption_status": "AVAILABLE",
        "temperament": "Friendly",
        "likes": "Playing fetch",
        "fee": "$100",
        "location": "Shelter",
    }
    response = client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    return Animal.objects.get(name="test_dog")


@pytest.mark.django_db
def test_animal_list_create_view(created_animal):
    assert created_animal.name == "test_dog"


@pytest.fixture
def test_animal_list_update_view(created_animal):
    assert created_animal.name == "test_dog"
    client = APIClient()
    url = reverse("animal-list-update", kwargs={"pk": created_animal.pk})
    updated_data = {
        "name": "updated_dog_name",
    }
    response = client.patch(url, updated_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert created_animal.name == "updated_dog_name"


@pytest.mark.django_db
def test_animal_list_delete_view(created_animal):
    client = APIClient()
    url = reverse("animal-list-delete", kwargs={"pk": created_animal.pk})

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Animal.objects.filter(pk=created_animal.pk).exists()
