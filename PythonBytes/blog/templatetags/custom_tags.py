from django import template


register = template.Library()

# @register.filter(name='truncate_long_words')
# def truncate_long_words(value, max_length):
#     print(value[0])
#     words = value.split()
#     wrapped_text = []
#
#     for word in words:
#         while len(word) > max_length:
#             wrapped_text.append(word[:max_length])
#             word = word[max_length:]
#         wrapped_text.append(word)
#
#     return ' '.join(wrapped_text)