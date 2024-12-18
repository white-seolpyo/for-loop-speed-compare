from time import time

import pandas as pd

space = 30
loop = 10
def loop_range(n):
    l = range(n)
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_range avg':{space}}, {T=}, {loop=}')
    return
def loop_list(n):
    l = list(range(n))
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_list avg':{space}}, {T=}, {loop=}')
    return
def loop_tuple(n):
    l = tuple(range(n))
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_tuple avg':{space}}, {T=}, {loop=}')
    return
def loop_set(n):
    l = set(range(n))
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_set avg':{space}}, {T=}, {loop=}')
    return
def loop_dict(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict avg':{space}}, {T=}, {loop=}')
    return
def loop_dict_call(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            ii = l[i]
            if stop < ii: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict_call avg':{space}}, {T=}, {loop=}')
    return
def loop_dict_get(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            ii = l.get(i)
            if stop < ii: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict_get avg':{space}}, {T=}, {loop=}')
    return
def loop_dict_keys(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l.keys():
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict_keys avg':{space}}, {T=}, {loop=}')
    return
def loop_dict_values(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l.values():
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict_values avg':{space}}, {T=}, {loop=}')
    return
def loop_dict_items(n):
    l = {i: i for i in range(n)}
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l.items():
            if stop < i[0]: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_dict_items avg':{space}}, {T=}, {loop=}')
    return
def loop_generator(n):
    l = (i for i in range(n))
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in l:
            if stop < i: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_generator avg':{space}}, {T=}, {loop=}')
    return
def loop_pandas_iterrow(n):
    l = pd.RangeIndex(n)
    df = pd.DataFrame({'a': l})
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in df.iterrows():
            # print(f'{i=}')
            # print(f'{i[0]=}')
            if stop < i[0]: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_pandas_iterrow avg':{space}}, {T=}, {loop=}')
    return
def loop_pandas_itertuple(n):
    l = pd.RangeIndex(n)
    df = pd.DataFrame({'a': l})
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in df.itertuples():
            # print(f'{i=}')
            # print(f'{i[0]=}')
            if stop < i[0]: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_pandas_itertuple avg':{space}}, {T=}, {loop=}')
    return
def loop_pandas_values(n):
    l = pd.RangeIndex(n)
    df = pd.DataFrame({'a': l})
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        for i in df.values:
            # print(f'{i=}')
            # print(f'{i[0]=}')
            if stop < i[0]: break
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_pandas_values avg':{space}}, {T=}, {loop=}')
    return
def loop_pandas_vector(n):
    l = pd.RangeIndex(n)
    df = pd.DataFrame({'a': l})
    stop = n - 9_000
    list_t = []
    for _ in range(loop):
        t = time()
        data: pd.DataFrame = df[stop < df['a']]
        v = data['a'].values[0]
        # print(f'{v=}')
        t2 = time() - t
        list_t.append(t2)
    T = sum(list_t) / loop
    print(f'{'loop_pandas_vector avg':{space}}, {T=}, {loop=}')
    return

a = 1_024 ** 2 * 40 # 41,943,040
print(f'a={a:,}')
print(f'{range(10)=}')
print(f'{list(range(10))=}')
print(f'{[i for i in range(10)]=}')
print(f'{(i for i in range(10))=}')
print(f'{tuple(i for i in range(10))=}')
loop_tuple(a)
loop_list(a)
loop_set(a)
loop_dict(a)
loop_dict_keys(a)
loop_dict_values(a)
loop_range(a)
loop_dict_call(a)
loop_dict_items(a)
loop_dict_get(a)
loop, l = (1, loop)
loop_generator(a)

loop = l
print()
loop_pandas_vector(a)
loop = 5
a = int(a / 102)
print(f'a={a:,}')
loop_pandas_values(a)
loop_pandas_itertuple(a)
a = int(a / 10)
print(f'a={a:,}')
loop_pandas_iterrow(a)

"""
a=41,943,040
range(10)=range(0, 10)
list(range(10))=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in range(10)]=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(i for i in range(10))=<generator object <genexpr> at 0x0000020A35CACAC0>
tuple(i for i in range(10))=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
loop_tuple avg                , T=1.2731175661087035, loop=10
loop_list avg                 , T=1.3596685409545899, loop=10
loop_dict avg                 , T=1.6014605045318604, loop=10
loop_dict_keys avg            , T=1.304155659675598, loop=10
loop_dict_values avg          , T=1.3998806715011596, loop=10
loop_range avg                , T=1.75155029296875, loop=10
loop_dict_call avg            , T=2.4083774089813232, loop=10
loop_dict_items avg           , T=2.4208778381347655, loop=10
loop_dict_get avg             , T=2.951988959312439, loop=10
loop_generator avg            , T=3.5225653648376465, loop=1

loop_pandas_vector avg        , T=0.06655125617980957, loop=10
a=411,206
loop_pandas_values avg        , T=0.11039986610412597, loop=5
loop_pandas_itertuple avg     , T=0.23932366371154784, loop=5
a=41,120
loop_pandas_iterrow avg       , T=1.1551873683929443, loop=5

a=41,943,040
range(10)=range(0, 10)
list(range(10))=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in range(10)]=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
(i for i in range(10))=<generator object <genexpr> at 0x000002BCB06ECAC0>
tuple(i for i in range(10))=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
loop_tuple avg                , T=1.2893378019332886, loop=10
loop_list avg                 , T=1.0276748657226562, loop=10
loop_set avg                  , T=1.1010380506515502, loop=10
loop_dict avg                 , T=1.2458739042282105, loop=10
loop_dict_keys avg            , T=1.5278726816177368, loop=10
loop_dict_values avg          , T=1.3221221208572387, loop=10
loop_range avg                , T=1.8835590124130248, loop=10
loop_dict_call avg            , T=2.3662047147750855, loop=10
loop_dict_items avg           , T=2.1593393087387085, loop=10
loop_dict_get avg             , T=3.0075628042221068, loop=10
loop_generator avg            , T=3.004049301147461, loop=1

loop_pandas_vector avg        , T=0.08100111484527588, loop=10
a=411,206
loop_pandas_values avg        , T=0.13660745620727538, loop=5
loop_pandas_itertuple avg     , T=0.2649997234344482, loop=5
a=41,120
loop_pandas_iterrow avg       , T=0.9916258335113526, loop=5
"""