from time import time

def loop_range(n):
    l = range(n)
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_range      , {t2=}')
    return
def loop_range_tuple(n):
    l = range(n)
    stop = n - 9_000
    t = time()
    for i in tuple(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_range_tuple, {t2=}')
    return
def loop_list(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_tuple      , {t2=}')
    return
def loop_list_tuple(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for i in tuple(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_tuple_tuple, {t2=}')
    return
def loop_set(n):
    l = set(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_set      , {t2=}')
    return
def loop_set_tuple(n):
    l = set(range(n))
    stop = n - 9_000
    t = time()
    for i in tuple(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_set_tuple, {t2=}')
    return
def loop_dict(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict      , {t2=}')
    return
def loop_dict_tuple(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in tuple(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_tuple, {t2=}')
    return
def loop_dict_keys(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.keys():
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_keys      , {t2=}')
    return
def loop_dict_keys_tuple(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in tuple(l.keys()):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_keys_tuple, {t2=}')
    return
def loop_dict_values(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.values():
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_values      , {t2=}')
    return
def loop_dict_values_tuple(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in tuple(l.values()):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_values_tuple, {t2=}')
    return
def loop_dict_items(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.items():
        if stop < i[0]: break
    t2 = time() - t
    print(f'loop_dict_items      , {t2=}')
    return
def loop_dict_items_tuple(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in tuple(l.items()):
        if stop < i[0]: break
    t2 = time() - t
    print(f'loop_dict_items_tuple, {t2=}')
    return

a = 1_024 ** 2 * 40 # 41,943,040
print(f'a={a:,}')
loop_range(a)
loop_range_tuple(a)
loop_list(a)
loop_list_tuple(a)
loop_set(a)
loop_set_tuple(a)
loop_dict(a)
loop_dict_tuple(a)
loop_dict_keys(a)
loop_dict_keys_tuple(a)
loop_dict_values(a)
loop_dict_values_tuple(a)
loop_dict_items(a)
loop_dict_items_tuple(a)

"""
a=41,943,040
loop_range      , t2=1.6467630863189697
loop_range_tuple, t2=3.621783971786499
loop_tuple      , t2=1.3204915523529053
loop_tuple_tuple, t2=3.17826509475708
loop_set      , t2=1.068998098373413
loop_set_tuple, t2=1.8896245956420898
loop_dict      , t2=1.2012474536895752
loop_dict_tuple, t2=1.7158081531524658
loop_dict_keys      , t2=1.1359665393829346
loop_dict_keys_tuple, t2=1.613569974899292
loop_dict_values      , t2=1.4906611442565918
loop_dict_values_tuple, t2=2.098557949066162
loop_dict_items      , t2=2.4415295124053955
loop_dict_items_tuple, t2=13.439655303955078
"""