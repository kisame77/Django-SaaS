from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from visits.models import PageVisit


def home_page_view(request):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percentage": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, "home.html", my_context)
