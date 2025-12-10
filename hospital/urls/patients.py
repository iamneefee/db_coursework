from django.urls import path

from hospital.views.patients import PatientList, PatientCreate, PatientUpdate, PatientDelete

urlpatterns = [
    path("", PatientList.as_view(), name="patient_list"),
    path("create/", PatientCreate.as_view(), name="patient_create"),
    path("<int:pk>/update/", PatientUpdate.as_view(), name="patient_update"),
    path("<int:pk>/delete/", PatientDelete.as_view(), name="patient_delete"),
]
