from time import time

def loop_range(n):
    l = range(n)
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_range     , {t2=}')
    return
def loop_range_list(n):
    l = range(n)
    stop = n - 9_000
    t = time()
    for i in list(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_range_list, {t2=}')
    return
def loop_tuple(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_tuple     , {t2=}')
    return
def loop_tuple_list(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for i in list(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_tuple_list, {t2=}')
    return
def loop_set(n):
    l = set(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_set     , {t2=}')
    return
def loop_set_list(n):
    l = set(range(n))
    stop = n - 9_000
    t = time()
    for i in list(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_set_list, {t2=}')
    return
def loop_dict(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict     , {t2=}')
    return
def loop_dict_list(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in list(l):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_list, {t2=}')
    return
def loop_dict_keys(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.keys():
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_keys     , {t2=}')
    return
def loop_dict_keys_list(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in list(l.keys()):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_keys_list, {t2=}')
    return
def loop_dict_values(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.values():
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_values     , {t2=}')
    return
def loop_dict_values_list(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in list(l.values()):
        if stop < i: break
    t2 = time() - t
    print(f'loop_dict_values_list, {t2=}')
    return
def loop_dict_items(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in l.items():
        if stop < i[0]: break
    t2 = time() - t
    print(f'loop_dict_items     , {t2=}')
    return
def loop_dict_items_list(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    t = time()
    for i in list(l.items()):
        if stop < i[0]: break
    t2 = time() - t
    print(f'loop_dict_items_list, {t2=}')
    return

a = 1_024 ** 2 * 40 # 41,943,040
print(f'a={a:,}')
loop_range(a)
loop_range_list(a)
loop_tuple(a)
loop_tuple_list(a)
loop_set(a)
loop_set_list(a)
loop_dict(a)
loop_dict_list(a)
loop_dict_keys(a)
loop_dict_keys_list(a)
loop_dict_values(a)
loop_dict_values_list(a)
loop_dict_items(a)
loop_dict_items_list(a)

"""
a=41,943,040
loop_range     , t2=1.5040099620819092
loop_range_list, t2=2.256002187728882
loop_tuple     , t2=0.9849987030029297
loop_tuple_list, t2=1.5719983577728271
loop_set     , t2=1.0330145359039307
loop_set_list, t2=1.79599928855896
loop_dict     , t2=1.2270004749298096
loop_dict_list, t2=1.6189839839935303
loop_dict_keys     , t2=1.111990213394165
loop_dict_keys_list, t2=1.5780003070831299
loop_dict_values     , t2=1.108030080795288
loop_dict_values_list, t2=1.6609992980957031
loop_dict_items     , t2=1.9119985103607178
loop_dict_items_list, t2=6.951999187469482
"""