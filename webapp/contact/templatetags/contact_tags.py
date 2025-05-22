from django import template
from contact.forms import ContactForm

register = template.Library()

@register.inclusion_tag('contact.html', takes_context=True)
def render_contact_modal(context):
    return {
        'form': context.get('form', ContactForm()),  # use existing form if present
        'show_modal': context.get('show_modal', False),
    }
