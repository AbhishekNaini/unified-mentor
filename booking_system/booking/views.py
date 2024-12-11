from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student, Appointment
from .forms import AppointmentForm

# List of Teachers
@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

# List of Students
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Booking an appointment
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

# List of appointments
@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

# Update appointment status
@login_required
def update_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.status = request.POST['status']
        appointment.save()
        return redirect('appointment_list')
    return render(request, 'update_appointment.html', {'appointment': appointment})
