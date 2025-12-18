def task_e1(computers, many_to_many):
    res1 = {}
    for c in computers:
        if 'компьютер' in c.name.lower():
            c_hard_disks = list(filter(lambda i: i[3] == c.name, many_to_many))
            if c_hard_disks:
                hard_disk_names = [hd[0] for hd in c_hard_disks]
                res1[c.name] = hard_disk_names
    return res1


def task_e2(computers, many_to_many):
    res2_unsorted = []
    for c in computers:
        c_hard_disks = list(filter(lambda i: i[3] == c.name, many_to_many))
        if c_hard_disks:
            c_prices = [price for _, _, price, _ in c_hard_disks]
            avg_price = round(sum(c_prices) / len(c_prices), 2)
            res2_unsorted.append((c.name, avg_price, len(c_hard_disks)))

    return sorted(res2_unsorted, key=lambda x: x[1])


def task_e3(hard_disks, many_to_many):
    res3 = []
    for hd in hard_disks:
        if hd.name.startswith('Б'):
            hd_computers = list(filter(lambda i: i[0] == hd.name, many_to_many))
            for hd_comp in hd_computers:
                res3.append((hd.name, hd.price, hd_comp[3]))

    return sorted(res3, key=lambda x: x[0])