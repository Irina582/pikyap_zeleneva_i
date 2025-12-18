#!/usr/bin/env python3

import unittest
import sys

if __name__ == '__main__':
    # Автоматическое обнаружение и запуск всех тестов
    test_suite = unittest.defaultTestLoader.discover('.', pattern='test_*.py')
    test_runner = unittest.TextTestRunner(verbosity=2)

    result = test_runner.run(test_suite)

    # Возвращаем код завершения в зависимости от результата тестов
    sys.exit(0 if result.wasSuccessful() else 1)