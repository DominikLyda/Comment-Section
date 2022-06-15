from django import template
from ..models import Like, Dislike, Comments

register = template.Library()


@register.filter
def like(comment):
    return Like.objects.filter(comment=comment).count()


@register.filter
def dislike(comment):
    return Dislike.objects.filter(comment=comment).count()


