from django.urls import path

from hospital.views.diagnoses import DiagnosisList, DiagnosisCreate, DiagnosisUpdate, DiagnosisDelete

urlpatterns = [
    path("", DiagnosisList.as_view(), name="diagnosis_list"),
    path("create/", DiagnosisCreate.as_view(), name="diagnosis_create"),
    path("<int:pk>/update/", DiagnosisUpdate.as_view(), name="diagnosis_update"),
    path("<int:pk>/delete/", DiagnosisDelete.as_view(), name="diagnosis_delete"),
]
