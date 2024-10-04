#from django.conf.urls import url
from django.urls import path, include
from .views import (
    TeamListApiView,
    TeamDetailApiView,
    PersonListApiView,
    PersonDetailApiView
)

urlpatterns = [
    path('teams', TeamListApiView.as_view()),
    path('teams/<int:team_id>/', TeamDetailApiView.as_view()),
    path('people', PersonListApiView.as_view()),
    path('people/<int:person_id>/', PersonDetailApiView.as_view()),
]
