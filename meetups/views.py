from django.shortcuts import render, redirect

from meetups.forms import MeetupRegistrationForm
from meetups.models import Meetup, Participant


def index(request):
    meetups = Meetup.objects.all()
    # meetups = Meetup.objects.all().order_by(...)
    return render(request, template_name='meetups/index.html', context={
        'show_meetups': len(meetups) > 0,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            meetup_registration_form = MeetupRegistrationForm()
            return render(request, template_name='meetups/details.html', context={
                'meetup': meetup,
                'form': meetup_registration_form
            })
        elif request.method == 'POST':
            meetup_registration_form = MeetupRegistrationForm(request.POST)
            if meetup_registration_form.is_valid():
                participant_email = meetup_registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=participant_email)
                meetup.participants.add(participant)
                return redirect(to='confirm-registration', meetup_slug=meetup.slug)
            else:
                return render(request, template_name='meetups/details.html', context={
                    'meetup': meetup,
                    'form': meetup_registration_form
                })
    except Exception as e:
        print(e)
        return render(request, template_name='meetups/404.html')


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(
        request,
        template_name='meetups/registration-success.html',
        context={'meetup': meetup}
    )
