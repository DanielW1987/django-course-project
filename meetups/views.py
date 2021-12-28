from django.shortcuts import render

from meetups.models import Meetup


def index(request):
    meetups = Meetup.objects.all()
    # meetups = Meetup.objects.all().order_by(...)
    return render(request, template_name='meetups/index.html', context={
        'show_meetups': len(meetups) > 0,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, template_name='meetups/details.html', context={
            'meetup': selected_meetup
        })
    except Exception:
        return render(request, template_name='meetups/404.html')
