from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Client", api.ClientViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Client/Client/", views.ClientListView.as_view(), name="Client_Client_list"),
    path("Client/Client/create/", views.ClientCreateView.as_view(), name="Client_Client_create"),
    path("Client/Client/detail/<int:pk>/", views.ClientDetailView.as_view(), name="Client_Client_detail"),
    path("Client/Client/update/<int:pk>/", views.ClientUpdateView.as_view(), name="Client_Client_update"),
    path("Client/Client/delete/<int:pk>/", views.ClientDeleteView.as_view(), name="Client_Client_delete"),

)
