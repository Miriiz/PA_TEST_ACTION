def test():
    return "a"


def delete_double_spaces(text):
    return text.replace('  ', ' ')


def delete_doublon_array(array):
    return list(set(array))


def delete_doublon_string(string):
    return ''.join(set(string))


def find_value_in_array(array, value):
    return array.index(value)


def find_value_in_string(string, value):
    return string.index(value)

def get_promotion_name(promotion_name):
    return promotion_name.split('_')[0]

def apply_pourcent_in_array(array, pourcent):
    return [x * pourcent for x in array]


# Modifier la police

def bonjour_test():
    print("bonjour")
