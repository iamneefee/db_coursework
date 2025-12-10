from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospital.forms import PatientForm
from hospital.models import Diagnosis
from hospital.models.patients import Patient
from hospital.utils.assign import assign_patient_to_ward


class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "hospital/patients/list.html"
    context_object_name = "patients"


class PatientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = "hospital/patients/form.html"
    permission_required = "hospital.create_patient"
    success_url = reverse_lazy("patients:patient_list")

    @transaction.atomic
    def form_valid(self, form):
        patient = form.save(commit=False)

        try:
            assign_patient_to_ward(patient)
        except Exception as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)

        patient.save()
        return super().form_valid(form)


class PatientUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "hospital/patients/form.html"
    permission_required = "hospital.update_patient"
    success_url = reverse_lazy("patients:patient_list")

    @transaction.atomic
    def form_valid(self, form):
        patient = form.save(commit=False)

        try:
            assign_patient_to_ward(patient)
        except Exception as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)

        patient.save()

        return super().form_valid(form)


class PatientDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Patient
    template_name = "hospital/confirm_delete.html"
    success_url = reverse_lazy("patients:patient_list")
    permission_required = "hospital.delete_patient"
