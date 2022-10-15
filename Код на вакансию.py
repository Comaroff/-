def groupe_skvoz(n_cust):
    n = [(sum(int(c) for c in str(i))) for i in range(0, n_cust)]
    res = {}
    for i in n:
        res[i] = res.get(i, 0) + 1
    return res

print(groupe_skvoz(300))

def groupe_proizv(n_cust, n_first_id):
    n = [(sum(int(c) for c in str(i))) for i in range(n_first_id, n_first_id + n_cust)]
    res = {}
    for i in n:
        res[i] = res.get(i, 0) + 1

    return res

print(groupe_proizv(300, 1254879))