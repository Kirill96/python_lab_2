import random
import string

def generate_file(count_str, count_field, str_sep, field_sep, numeric):
    _str = 0
    _field = 0
    with open('in.txt', 'w') as file:
        while _str != count_str:
            _field = 0
            while _field != count_field:
                if numeric:
                    file.write(''.join(random.choice(string.digits) for i in
                    range(5)))
                else:
                    file.write(''.join(random.choice(string.ascii_uppercase +
                    string.ascii_lowercase) for i in range(5)))                    
                if _field != count_field - 1:
                    file.write(field_sep)
                _field += 1
            if _str != count_str - 1:
                file.write(str_sep)
            _str += 1
