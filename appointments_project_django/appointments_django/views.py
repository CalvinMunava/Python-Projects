from django.shortcuts import redirect,render
from .models import Appointment
from .forms import AppointmentForm

# Create your views here.

def appointments_main(request):
    context = {}
    context["Appointments"] = Appointment.objects.all()
    form = AppointmentForm()
    context["form"] = form
    return render(request, 'appointments_main.html', context)

def appointment_create(request):
    form = AppointmentForm(request.POST)
    form.save()
    return redirect('appointments_main')