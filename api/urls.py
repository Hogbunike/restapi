from django.urls import path, re_path
from .views import PersonDetail, PersonInfo


urlpatterns = [
    path('api/', PersonDetail.as_view(), name='api'),
    re_path(r'^api/(?P<param>[0-9]+|[a-zA-Z]+)$', PersonInfo.as_view()),
    # path('api/<int:id>/', PersonInfo.as_view()),
]