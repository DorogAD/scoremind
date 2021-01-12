from django import template
from remind.models import Episode

register = template.Library()


@register.inclusion_tag('remind/menu_tpl.html')
def show_menu(menu_class='menu'):
    episodes = Episode.objects.all()
    return {"episodes": episodes, "menu_class": menu_class}
