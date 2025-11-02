class HardDisk:
    """Жесткий диск"""
    def __init__(self, id, name, capacity, price, computer_id):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.price = price
        self.computer_id = computer_id

class Computer:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class HardDiskComputer:
    """Для реализации связи многие-ко-многим"""
    def __init__(self, computer_id, hard_disk_id):
        self.computer_id = computer_id
        self.hard_disk_id = hard_disk_id

def main():
    computers = [
        Computer(1, "Домашний компьютер"),
        Computer(2, "Рабочий"),
        Computer(3, "Игровой компьютер"),
        Computer(4, "Офисный"),
        Computer(5, "Серверный компьютер"),
        Computer(6, "Сломанный")
    ]
    hard_disks = [
        HardDisk(1, "Барракуда 1TB", 1000, 45.90, 1),
        HardDisk(2, "Восток 500GB", 500, 25.50, 2),
        HardDisk(3, "Север 2TB", 2000, 85.00, 3),
        HardDisk(4, "WD Blue 1TB", 1000, 42.80, 3),
        HardDisk(5, "Samsung 870 2TB", 2000, 92.75, 3),
        HardDisk(6, "Toshiba 500GB", 500, 28.30, 4),
        HardDisk(7, "Hitachi 1TB", 1000, 47.50, 5),
        HardDisk(8, "Kingston 2TB", 2000, 88.00, 6)
    ]
    # Связи многие-ко-многим
    hard_disks_computers = [
        HardDiskComputer(1, 1),
        HardDiskComputer(2, 2),
        HardDiskComputer(3, 3),
        HardDiskComputer(3, 4),
        HardDiskComputer(3, 5),
        HardDiskComputer(4, 6),
        HardDiskComputer(5, 7),
        HardDiskComputer(6, 3),
        HardDiskComputer(6, 4),
        HardDiskComputer(6, 5)
    ]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, hdc.computer_id, hdc.hard_disk_id)
                         for c in computers
                         for hdc in hard_disks_computers
                         if c.id == hdc.computer_id]

    many_to_many = [(hd.name, hd.capacity, hd.price, comp_name)
                    for comp_name, comp_id, hd_id in many_to_many_temp
                    for hd in hard_disks if hd.id == hd_id]


    print('Задание E1')
    print('Список всех компьютеров, у которых в названии присутствует слово "компьютер", и список их жестких дисков:')

    res1 = {}
    for c in computers:
        if 'компьютер' in c.name.lower():
            c_hard_disks = list(filter(lambda i: i[3] == c.name, many_to_many))
            if c_hard_disks:
                hard_disk_names = [hd[0] for hd in c_hard_disks]
                res1[c.name] = hard_disk_names

    for computer_name, hard_disks_list in res1.items():
        print(f'\nКомпьютер: {computer_name}')
        for hd_name in hard_disks_list:
            print(f'  Жесткий диск: {hd_name}')


    print('\nЗадание E2')
    print('Список компьютеров со средней ценой жестких дисков в каждом, отсортированный по средней цене:')

    res2_unsorted = []
    for c in computers:
        c_hard_disks = list(filter(lambda i: i[3] == c.name, many_to_many))
        if c_hard_disks:
            c_prices = [price for _, _, price, _ in c_hard_disks]
            avg_price = round(sum(c_prices) / len(c_prices), 2)
            res2_unsorted.append((c.name, avg_price, len(c_hard_disks)))
    res2 = sorted(res2_unsorted, key=lambda x: x[1])

    for computer_name, avg_price, count in res2:
        print(f'Компьютер: {computer_name}, Средняя цена: {avg_price} руб. (дисков: {count})')


    print('\nЗадание E3')
    print('Список всех жестких дисков, у которых название начинается с буквы "Б", и названия их компьютеров:')

    res3 = []
    for hd in hard_disks:
        if hd.name.startswith('Б'):
            hd_computers = list(filter(lambda i: i[0] == hd.name, many_to_many))
            for hd_comp in hd_computers:
                res3.append((hd.name, hd.price, hd_comp[3]))

    res3_sorted = sorted(res3, key=lambda x: x[0])

    for hd_name, hd_price, comp_name in res3_sorted:
        print(f'Жесткий диск: {hd_name}, Цена: {hd_price} руб. -> Компьютер: {comp_name}')

if __name__ == '__main__':
    main()