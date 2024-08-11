def get_menu_context(request):
    menu = [{'title': "Новости и события", 'url_name': "blog:home"},
            {'title': "Новая запись", 'url_name': "blog:post_create"},
            {'title': "Мои записи", 'url_name': "blog:home"},
            {'title': "Встречи участников", 'url_name': "blog:home"},
            ]

    return {
        'menu': menu,
    }
