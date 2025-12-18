from data_classes import Computer, HardDisk, HardDiskComputer


def create_test_data():
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

    return computers, hard_disks, hard_disks_computers


def create_many_to_many_relation(computers, hard_disks, hard_disks_computers):
    many_to_many_temp = [
        (c.name, hdc.computer_id, hdc.hard_disk_id)
        for c in computers
        for hdc in hard_disks_computers
        if c.id == hdc.computer_id
    ]

    many_to_many = [
        (hd.name, hd.capacity, hd.price, comp_name)
        for comp_name, comp_id, hd_id in many_to_many_temp
        for hd in hard_disks if hd.id == hd_id
    ]

    return many_to_many