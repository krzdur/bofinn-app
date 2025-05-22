from urllib.parse import urlparse

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            message = render_to_string('emails/message.html', {
                'name': name,
                'email': email,
                'message': content
            }
                                    )
            send_mail(
                subject='New message in the contact form',
                message='Hey BOFINNer, you\'ve got a new message through the contact form!',
                from_email='noreply@bofinn.com',
                recipient_list=['contact@boffin.com'],
                html_message=message
            )
            referer = request.META.get('HTTP_REFERER', '/')
            return redirect(f"{referer}?contact_success=1#contactModal")
        else:
            context = {
                'form': form,
                'show_modal': True,
            }
            return render(request, get_template_from_referer(request), context)

    else:
        return render(request, get_template_from_referer(request))

def get_template_from_referer(request):
    referrer = request.META.get('HTTP_REFERER', '')
    referrer_path = urlparse(referrer).path.strip('/')
    if referrer_path and referrer_path != 'contact':
        return f'main/{referrer_path}.html'
    else:
        return 'main/index.html'

def thankyou(request):
    return render(request, 'thankyou.html')