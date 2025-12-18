import unittest
from data_service import create_test_data, create_many_to_many_relation
from query_service import task_e1, task_e2, task_e3


class TestQueries(unittest.TestCase):

    def setUp(self):
        self.computers, self.hard_disks, self.hard_disks_computers = create_test_data()
        self.many_to_many = create_many_to_many_relation(
            self.computers, self.hard_disks, self.hard_disks_computers
        )

    def test_task_e1(self):
        result = task_e1(self.computers, self.many_to_many)

        self.assertIsInstance(result, dict)

        expected_computers = ['Домашний компьютер', 'Игровой компьютер', 'Серверный компьютер']
        self.assertListEqual(sorted(list(result.keys())), sorted(expected_computers))

        self.assertIn('Барракуда 1TB', result['Домашний компьютер'])

        self.assertNotIn('Рабочий', result)
        self.assertNotIn('Офисный', result)

    def test_task_e2(self):
        result = task_e2(self.computers, self.many_to_many)


        self.assertIsInstance(result, list)

        prices = [item[1] for item in result]
        self.assertEqual(prices, sorted(prices))


        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 3)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], float)
            self.assertIsInstance(item[2], int)

    def test_task_e3(self):
        result = task_e3(self.hard_disks, self.many_to_many)

        self.assertIsInstance(result, list)

        for hd_name, hd_price, comp_name in result:
            self.assertTrue(hd_name.startswith('Б'))

        disk_names = [item[0] for item in result]
        self.assertEqual(disk_names, sorted(disk_names))

        expected_result = ('Барракуда 1TB', 45.9, 'Домашний компьютер')
        self.assertIn(expected_result, result)


if __name__ == '__main__':
    unittest.main()