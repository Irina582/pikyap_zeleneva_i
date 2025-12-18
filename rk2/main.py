from data_service import create_test_data, create_many_to_many_relation
from query_service import task_e1, task_e2, task_e3


def print_results(res1, res2, res3):
    print('Задание E1')
    print('Список всех компьютеров, у которых в названии присутствует слово "компьютер", и список их жестких дисков:')

    for computer_name, hard_disks_list in res1.items():
        print(f'\nКомпьютер: {computer_name}')
        for hd_name in hard_disks_list:
            print(f'  Жесткий диск: {hd_name}')

    print('\nЗадание E2')
    print('Список компьютеров со средней ценой жестких дисков в каждом, отсортированный по средней цене:')

    for computer_name, avg_price, count in res2:
        print(f'Компьютер: {computer_name}, Средняя цена: {avg_price} руб. (дисков: {count})')

    print('\nЗадание E3')
    print('Список всех жестких дисков, у которых название начинается с буквы "Б", и названия их компьютеров:')

    for hd_name, hd_price, comp_name in res3:
        print(f'Жесткий диск: {hd_name}, Цена: {hd_price} руб. -> Компьютер: {comp_name}')


def main():
    computers, hard_disks, hard_disks_computers = create_test_data()
    many_to_many = create_many_to_many_relation(computers, hard_disks, hard_disks_computers)

    res1 = task_e1(computers, many_to_many)
    res2 = task_e2(computers, many_to_many)
    res3 = task_e3(hard_disks, many_to_many)

    print_results(res1, res2, res3)


if __name__ == '__main__':
    main()