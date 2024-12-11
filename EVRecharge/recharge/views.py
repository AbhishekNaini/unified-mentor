from django.shortcuts import render, redirect
from .models import Station, Booking
from .forms import BookingForm

def home(request):
    stations = Station.objects.all()
    return render(request, 'home.html', {'stations': stations})

def book_slot(request, station_id):
    station = Station.objects.get(id=station_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.station = station
            booking.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'station': station})
