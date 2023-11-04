from django import forms
from .models import Appointment
from bootstrap_datepicker_plus import DatePickerInput


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["StudentNumber",  "StudentName", "AppointmentDate", "AppointmentDescription",]
        widgets = { 'AppointmentDate': DatePickerInput}
