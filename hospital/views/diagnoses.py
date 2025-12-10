from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospital.forms import DiagnosisForm
from hospital.models.diagnoses import Diagnosis


class DiagnosisList(LoginRequiredMixin, ListView):
    model = Diagnosis
    template_name = "hospital/diagnosis/list.html"
    context_object_name = "diagnoses"


class DiagnosisCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = "hospital/diagnosis/form.html"
    success_url = reverse_lazy("diagnoses:diagnosis_list")
    permission_required = "hospital.create_diagnosis"


class DiagnosisUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = "hospital/diagnosis/form.html"
    success_url = reverse_lazy("diagnoses:diagnosis_list")
    permission_required = "hospital.update_diagnosis"


class DiagnosisDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Diagnosis
    template_name = "hospital/confirm_delete.html"
    success_url = reverse_lazy("diagnoses:diagnosis_list")
    permission_required = "hospital.delete_diagnosis"
