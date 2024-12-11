from django.shortcuts import render
from visits.models import PageVisit
from django.db.models import Count


def home_page_view(request, *args, **kwargs):
    # This can directly call the about_view or can render home page context as needed
    return about_view(request, *args, **kwargs)


def about_view(request):
    # Fetch the total page visit count
    qs = PageVisit.objects.all()

    # Filter by the current page path
    page_qs = PageVisit.objects.filter(path=request.path)

    # Calculate the percentage of visits for the current page
    try:
        total_visits = qs.count()
        page_visits = page_qs.count()
        if total_visits > 0:
            percentage = (page_visits * 100.0) / total_visits
        else:
            percentage = 0
    except ZeroDivisionError:
        # In case of a zero division error, default to 0%
        percentage = 0

    # Set the title and context for the page
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percentage": percentage,
        "total_visit_count": total_visits,
    }

    # Only create a new PageVisit if this visit is not already recorded
    if not PageVisit.objects.filter(path=request.path).exists():
        PageVisit.objects.create(path=request.path)

    return render(request, "home.html", my_context)
