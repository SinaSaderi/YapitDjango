from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Property", api.PropertyViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Property/Property/", views.PropertyListView.as_view(), name="Property_Property_list"),
    path("Property/Property/create/", views.PropertyCreateView.as_view(), name="Property_Property_create"),
    path("Property/Property/detail/<int:pk>/", views.PropertyDetailView.as_view(), name="Property_Property_detail"),
    path("Property/Property/update/<int:pk>/", views.PropertyUpdateView.as_view(), name="Property_Property_update"),
    path("Property/Property/delete/<int:pk>/", views.PropertyDeleteView.as_view(), name="Property_Property_delete"),

)
