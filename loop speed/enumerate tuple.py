from time import time


space = 20
def loop_tuple(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_tuple':{space}}, {t2=}')
    return
def loop_index(n):
    n = int(n / 1_000)
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for i in l:
        n = l.index(i)
        if stop < n: break
    t2 = time() - t
    print(f'{'loop_index':{space}}, {t2=}')
    return
def loop_range(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for n in range(len(l)):
        i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_range':{space}}, {t2=}')
    return
def loop_range_tuple(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for n in tuple(range(len(l))):
        i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_range_tuple':{space}}, {t2=}')
    return
def loop_enumerate(n):
    l = tuple(range(n))
    stop = n - 9_000
    t = time()
    for n, i in enumerate(l):
        # i = l[n]
        if stop < i: break
    t2 = time() - t
    print(f'{'loop_enumerate':{space}}, {t2=}')
    return
def loop_range_zip(n):
    l = tuple(range(n))
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
loop_tuple(a)
loop_range(a)
loop_enumerate(a)
loop_range_zip(a)
loop_range_tuple(a)
loop_index(a)

"""
a=41,943,040
loop_tuple          , t2=0.9890003204345703
loop_range          , t2=2.0239992141723633
loop_enumerate      , t2=5.446649074554443
loop_range_zip      , t2=3.3700788021087646
loop_range_tuple    , t2=3.5199944972991943
loop_index          , t2=8.423755168914795
"""