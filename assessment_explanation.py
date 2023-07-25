random_stuffs = ['hello', '23', '3.4', 'night',  'welcome']


def get_on_string_with_characters(lst):
    return [value for value in lst if value.isalpha()]


print(get_on_string_with_characters(random_stuffs))