from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "Toyota"},
        {"title": "Nissan"},
        {"title": "Chevrolet"},
    ]
    context = {
        "car_list": car_list,
    }
    return render(request, "my_first_app/car_list.html", context)