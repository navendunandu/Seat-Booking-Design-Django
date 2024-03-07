from django.shortcuts import render

# Create your views here.
def index(request):
    selected_seats = []
    seatcount = 40
    booked_seats = [4,5,6,22,23,30,10,38]
    seat_count = [2,7,12,17,22,27,32,37]
    seats_range = range(1, seatcount + 1)
    if request.method == "POST":
        selected_seats = request.POST.getlist('txtcheck[]')
        print(selected_seats)    
    return render(request, 'Index/index.html', {'seats_range': seats_range,"seat_count":seat_count,'booked':booked_seats})
