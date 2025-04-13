from django import template

register = template.Library();

#look for your icon here https://fontawesome.com/search?ic=free

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
    }]
    