from django.shortcuts import render


def index(request):
    meetups = [
        {'title': 'A first Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]

    return render(request, template_name='meetups/index.html', context={
        'show_meetups': len(meetups) > 0,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {'title': 'A first Meetup', 'location': 'New York', 'description': 'The description of the first meetup'},
    return render(request, template_name='meetups/details.html', context={
        'meetup': selected_meetup
    })
