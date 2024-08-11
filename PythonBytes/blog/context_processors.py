def get_menu_context(request):
    menu = [{'title': "Новости и события", 'url_name': "blog:home"},
            {'title': "Новая запись", 'url_name': "blog:post_create"},
            {'title': "Мои записи", 'url_name': "blog:my_posts"},
            {'title': "Встречи участников", 'url_name': "blog:home"},
            ]

    current_item = ""
    for item in menu:
        if request.resolver_match.view_name == item['url_name']:
            current_item = item['title']
            break

    return {
        'menu': menu,
        'current_item': current_item,
    }
