from django.http import HttpResponse
from .models import Events
from django.shortcuts import render

def calendar(request):
    from datetime import date, timedelta
    # d = date(2020, 1, 1)
    # d += timedelta(days=6 - d.weekday()) # First Sunday
    # all_sunday_in_2020 = []
    # while d.year != 2021:
    #     all_sunday_in_2020.append({'name': 'my-title', 'start': d, 'end': d 
    #     + timedelta(days=1)})
    #     d += timedelta(days=7)
    # return render(request,'calendar.html',{'events':all_sunday_in_2020})
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calendar.html',context)

def add_event(request):
    print('add_event: ',request)
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)

def index(request):
    return HttpResponse("Hello, world. You're at the calender index.")