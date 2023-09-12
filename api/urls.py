from django.urls import path
from .views import PersonList, PersonInfo


urlpatterns = [
    path('api/', PersonList.as_view(), name='all-create'),
    path('api/<int:id>/', PersonInfo.as_view(), name="retrieve-update-delete"),
]