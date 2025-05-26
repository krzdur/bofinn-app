from django import template

register = template.Library();


# look for your icon here https://fontawesome.com/search?ic=free

@register.simple_tag
def get_links():
    return [{
        'name': 'Home',
        'href': '/',
        'icon': 'fa-house'
    }, {
        'name': 'Properties',
        'href': '/properties',
        'icon': 'fa-building'
    },  {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card'
    }, {
        'name': 'Interior Design',
        'href': '/interior',
        'icon': 'fa-solid fa-landmark'
    }
    ]
