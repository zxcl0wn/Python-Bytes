from .utils import menu


def get_menu_context(request):
    current_item = ""
    for item in menu:
        if request.resolver_match.view_name == item['url_name']:
            current_item = item['title']
            break

    return {
        'menu': menu,
        'current_item': current_item,
    }
