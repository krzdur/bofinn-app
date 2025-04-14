from django import template

register = template.Library()

# Look for your icon here: https://fontawesome.com/search?ic=free

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house',
    }, {
        'name': 'Properties',
        'href': '/properties',
        'icon': 'fa-house-lock',
    }, {
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
    }, {
        'name': 'News',
        'href': '/news/',
        'icon': 'fa-newspaper',
    }, {
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment',  # look for your icon here: https://fontawesome.com/search?ic=free
    }]
