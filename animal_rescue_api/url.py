from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path(
        "api/animal_rescue_api/",
        views.AnimalListCreate.as_view(),
        name="animal-list-create",
    ),
    path(
        "api/animal_rescue_api/delete/<pk>",
        views.AnimalListDelete.as_view(),
        name="animal-list-delete",
    ),
    path(
        "api/animal_rescue_api/update/<pk>",
        views.AnimalListUpdate.as_view(),
        name="animal-list-update",
    ),
    path(
        "api/animal_rescue_api/animal/<pk>",
        views.Animal.as_view(),
        name="animal-detail",
    ),
    path("api/register", views.UserRegister.as_view(), name="register"),
    path("api/login", views.UserLogin.as_view(), name="login"),
    path("api/logout", views.UserLogout.as_view(), name="logout"),
    path("api/user", views.UserView.as_view(), name="user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
