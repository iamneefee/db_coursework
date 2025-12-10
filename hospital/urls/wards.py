from django.urls import path

from hospital.views.wards import WardList, WardCreate, WardUpdate, WardDelete, WardStats

urlpatterns = [
    path("", WardList.as_view(), name="ward_list"),
    path("create/", WardCreate.as_view(), name="ward_create"),
    path("<int:pk>/update/", WardUpdate.as_view(), name="ward_update"),
    path("<int:pk>/delete/", WardDelete.as_view(), name="ward_delete"),
    path("analysis/", WardStats.as_view(), name="ward_stats"),
]
