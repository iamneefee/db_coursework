from django import forms

from hospital.models.diagnoses import Diagnosis
from hospital.models.patients import Patient
from hospital.models.wards import Ward


class PatientForm(forms.ModelForm):
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all(),
        empty_label="Выберите диагноз",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "father_name", "diagnosis"]
        widgets = {
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
            "father_name": forms.TextInput(),
        }


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(),
        }


class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields = ["name", "max_count"]
        widgets = {
            "name": forms.TextInput(),
            "max_count": forms.NumberInput(),
        }

    def clean_max_count(self):
        max_count = self.cleaned_data["max_count"]
        if self.instance.pk:
            current_patients = Patient.objects.filter(ward=self.instance).count()
            if max_count < current_patients:
                raise forms.ValidationError(
                    f"Невозможно установить размер палаты меньше, чем текущее количество пациентов ({current_patients})."
                )
        return max_count
