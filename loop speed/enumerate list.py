from time import time


space = 20
def loop_list(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_list':{space}}, {t2=}')
    return
def loop_index(n):
    n = int(n / 1_000)
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        n = l.index(i)
        if stop < n: break
    t2 = time() - t
    print(f'{'loop_index':{space}}, {t2=}')
    return
def loop_range(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for n in range(len(l)):
        i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_range':{space}}, {t2=}')
    return
def loop_range_list(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for n in list(range(len(l))):
        i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_range_list':{space}}, {t2=}')
    return
def loop_enumerate(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for n, i in enumerate(l):
        # i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_enumerate':{space}}, {t2=}')
    return
def loop_range_zip(n):
    l = list(range(n))
    stop = n - 9_000
    t = time()
    for n, i in zip(range(len(l)), l):
        # i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_range_zip':{space}}, {t2=}')
    return

a = 1_024 ** 2 * 40 # 41,943,040
print(f'a={a:,}')
loop_list(a)
loop_range(a)
loop_enumerate(a)
loop_range_zip(a)
loop_range_list(a)
loop_index(a)

"""
a=41,943,040
loop_list           , t2=0.9989845752716064
loop_range          , t2=2.1120147705078125
loop_enumerate      , t2=2.406000852584839
loop_range_zip      , t2=2.3389899730682373
loop_range_list     , t2=2.738016366958618
loop_index          , t2=5.774005174636841
"""