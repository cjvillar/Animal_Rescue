from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/animal_rescue_api/', views.AnimalListCreate.as_view() ),
    path('api/animal_rescue_api/delete/<pk>', views.AnimalListDelete.as_view() ),
    path('api/animal_rescue_api/update/<pk>', views.AnimalListUpdate.as_view() ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)