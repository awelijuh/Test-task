import ast


def str_valid(s):
    s = s.strip()
    if (s[0] == '“' and s[-1] == '”') or (s[0] == s[-1] and s[0] in ['"', "'"]):
        s = s[1:-1]
    if len(s) != 9:
        return False, 'The length of the string must be 9'
    for i in range(len(s)):
        if s[i] not in ['0', '1']:
            return False, '"{}" at position {} does not match "0" and "1"'.format(s[i], i)
    return True, s


def array_type_valid(a):
    return isinstance(a, list)


def array_size_valid(a):
    return len(a) == 9


def get_type_size_valid_answer(a):
    if not array_type_valid(a):
        return False, 'Invalid array format'
    elif not array_size_valid(a):
        return False, 'The length of the array must be 9'
    return True, a


def array_valid(s):
    s = s.strip()
    try:
        a = ast.literal_eval(s)
    except (ValueError, SyntaxError):
        pass
    else:
        return get_type_size_valid_answer(a)

    try:
        a = ast.literal_eval(s.replace('“', '"').replace('”', '"'))
    except (ValueError, SyntaxError):
        return False, 'Invalid array format'
    return get_type_size_valid_answer(a)


r, s = str_valid(input())

if r is False:
    print(s)
    exit()

r, a = array_valid(input())

if r is False:
    print(a)
    exit()

ans = ['“' + a[i] + '”' for i in range(len(s)) if s[i] == '1']

print('[' + ', '.join(ans) + ']')
