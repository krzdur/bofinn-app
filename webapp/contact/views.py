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

            return redirect('thankyou')

    else:
        form = ContactForm()


    return render(request, 'contact.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')