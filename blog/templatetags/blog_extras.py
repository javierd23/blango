from django import template 
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def author_details(author):
    if not isinstance(author, User):
        return ""

    if author.first_name and author.last_name:
        return '<a href="mailto:ben@example.com">ben</a>'
    return author.username 