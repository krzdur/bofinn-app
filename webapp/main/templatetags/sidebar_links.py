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
<<<<<<< HEAD
=======
        'name': 'Properties',
        'href': '/properties',
        'icon': 'fa-house-lock',
    }, {
>>>>>>> b27142df4413c2b3d9b571ebc44c26e4fe660733
        'name': 'Contact',
        'href': '/contact',
        'icon': 'fa-paper-plane',
    }, {
        'name': 'About',
        'href': '/about',
        'icon': 'fa-address-card',
<<<<<<< HEAD
    },{
        'name': 'News',
        'href': '/news/',
        'icon': 'fa-newspaper',
    },{
        'name': 'Properties',
        'href': '/properties',
        'icon': 'fa-building'
    },{
        'name': 'Forum',
        'href': '/forum',
        'icon': 'fa-comment', #look for your icon here https://fontawesome.com/search?ic=free
=======
>>>>>>> b27142df4413c2b3d9b571ebc44c26e4fe660733
    }]
    