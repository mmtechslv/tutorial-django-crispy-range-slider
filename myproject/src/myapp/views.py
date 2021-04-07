# from django.shortcuts import render
# from .models import People
#
# def index(request):
#     all_people = People.objects.all()
#     return render(request, 'index.html', {'all_people':all_people})

from django.shortcuts import render
from .filters import PeopleFilter

def index(request):
    people_filter = PeopleFilter(request.GET)
    return render(request, 'index.html', {'people_filter':people_filter})
