from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('', include(('hospital.urls.auth', 'hospital'), namespace='hospital')),
    path('', lambda request: redirect('patients:patient_list')),
    path('patients/', include(('hospital.urls.patients', 'patients'), namespace='patients')),
    path('diagnosis/', include(('hospital.urls.diagnoses', 'diagnoses'), namespace='diagnoses')),
    path('wards/', include(('hospital.urls.wards', 'wards'), namespace='wards')),
]
