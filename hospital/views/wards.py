from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db import connection
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from hospital.forms import WardForm
from hospital.models.wards import Ward


class WardList(LoginRequiredMixin, ListView):
    model = Ward
    template_name = "hospital/wards/list.html"
    context_object_name = "wards"


class WardCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Ward
    form_class = WardForm
    template_name = "hospital/wards/form.html"
    success_url = reverse_lazy("wards:ward_list")
    permission_required = "hospital.create_ward"


class WardUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Ward
    form_class = WardForm
    template_name = "hospital/wards/form.html"
    success_url = reverse_lazy("wards:ward_list")
    permission_required = "hospital.update_ward"


class WardDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ward
    template_name = "hospital/confirm_delete.html"
    success_url = reverse_lazy("wards:ward_list")
    permission_required = "hospital.delete_ward"


class WardStats(LoginRequiredMixin, View):
    template_name = "hospital/wards/ward_stats.html"

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ward_load()")
            data = cursor.fetchall()
        context = {"stats": data}
        return render(request, self.template_name, context)
