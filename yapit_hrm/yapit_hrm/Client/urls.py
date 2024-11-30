from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("SampleModel", api.SampleModelViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("SampleModel/SampleModel/", views.SampleModelListView.as_view(), name="SampleModel_SampleModel_list"),
    path("SampleModel/SampleModel/create/", views.SampleModelCreateView.as_view(), name="SampleModel_SampleModel_create"),
    path("SampleModel/SampleModel/detail/<int:pk>/", views.SampleModelDetailView.as_view(), name="SampleModel_SampleModel_detail"),
    path("SampleModel/SampleModel/update/<int:pk>/", views.SampleModelUpdateView.as_view(), name="SampleModel_SampleModel_update"),
    path("SampleModel/SampleModel/delete/<int:pk>/", views.SampleModelDeleteView.as_view(), name="SampleModel_SampleModel_delete"),

)
