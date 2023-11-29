import pytest
# from animal_rescue_api.views import Animal
# from animal_rescue_api.models import Animal

# @pytest.fixture
# def test_add_animal():
#     return Animal(
#     animal_type='Dog',
#     name='Max',
#     sex='Male',
#     breed='Golden Retriever',
#     neutered=True,
#     age=3,
#     weight='25 lbs',
#     adoption_status='AVAILABLE',
#     temperament='Friendly',
#     likes='Playing fetch',
#     fee='$150',
#     location='Shelter A',
#     image = 'no_image.jpg'
# )

@pytest.mark.django_db
def test_animal_rescue_api(client):
    response = client.get('/api/animal_rescue_api/')
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
   