menu = [{'title': "Новости и события", 'url_name': "blog:home"},
        {'title': "Новая запись", 'url_name': "blog:post_create"},
        {'title': "Мои записи", 'url_name': "blog:my_posts"},
        {'title': "Встречи участников", 'url_name': "blog:home"},
        ]


class DataMixin:
    title_page = None
    paginate_by = 3
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title_page'] = self.title_page
        else:
            self.extra_context['title_page'] = "Блог клуба Python Bytes!"
