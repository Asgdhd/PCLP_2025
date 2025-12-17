import unittest
from RK1_refactored import Computer, Microprocessor, MicroprocessorComputer, DataManager


class TestRK1(unittest.TestCase):
    """Класс для модульного тестирования программы РК1"""

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом"""
        # Тестовые данные
        self.computers = [
            Computer(1, 'Test Computer 1'),
            Computer(2, 'A Test Computer'),
            Computer(3, 'Test Computer 2'),
        ]

        # Тестовые микропроцессоры
        self.microprocessors = [
            Microprocessor(1, 'Intel Xeon', 3500, 1),
            Microprocessor(2, 'AMD Ryzen', 3200, 1),
            Microprocessor(3, 'Intel Pentium', 2800, 2),
            Microprocessor(4, 'AMD', 3000, 3),
        ]

        self.microprocessors_computers = [
            MicroprocessorComputer(1, 1),
            MicroprocessorComputer(1, 2),
            MicroprocessorComputer(2, 3),
            MicroprocessorComputer(3, 4),
        ]

        self.manager = DataManager(
            self.computers,
            self.microprocessors,
            self.microprocessors_computers
        )

    # Тест 1: Задание Д1
    def test_task1_microprocessors_ending_with_n(self):
        """Тест задания Д1: поиск микропроцессоров, чья модель заканчивается на 'n'"""
        one_to_many = self.manager.get_one_to_many()
        result = self.manager.task1(one_to_many)

        # Проверяем, что все найденные модели заканчиваются на 'n'
        for item in result:
            self.assertTrue(item[0].endswith('n'),
                            f"Модель '{item[0]}' не заканчивается на 'n'")

        # Проверяем конкретные ожидаемые результаты
        expected_models = ['Intel Xeon', 'AMD Ryzen']
        result_models = [item[0] for item in result]

        # Проверяем наличие ожидаемых моделей
        for model in expected_models:
            self.assertIn(model, result_models,
                          f"Модель '{model}' должна быть в результатах")

        # Проверяем, что модели, НЕ заканчивающиеся на 'n', отсутствуют
        unexpected_models = ['Intel Pentium', 'AMD']
        for model in unexpected_models:
            self.assertNotIn(model, result_models,
                             f"Модель '{model}' не должна быть в результатах")

    # Тест 2: Задание Д2
    def test_task2_average_frequency_calculation(self):
        """Тест задания Д2: вычисление средней частоты микропроцессоров по компьютерам"""
        one_to_many = self.manager.get_one_to_many()
        result = self.manager.task2(one_to_many)

        # Проверяем структуру результата
        self.assertIsInstance(result, list, "Результат должен быть списком")

        for item in result:
            self.assertIsInstance(item, tuple, "Каждый элемент должен быть кортежем")
            self.assertEqual(len(item), 2, "Кортеж должен содержать 2 элемента")
            self.assertIsInstance(item[1], (int, float),
                                  "Второй элемент должен быть числом")

        # Проверяем правильность вычислений для Test Computer 1
        # У него 2 процессора: Intel Xeon (3500) и AMD Ryzen (3200), среднее = 3350
        for computer_name, avg_freq in result:
            if computer_name == 'Test Computer 1':
                self.assertAlmostEqual(avg_freq, 3350.0, places=2,
                                       msg=f"Неправильная средняя частота для {computer_name}")

    # Тест 3: Задание Д3
    def test_task3_computers_starting_with_A(self):
        """Тест задания Д3: компьютеры, начинающиеся с 'A', со списком моделей процессоров"""
        many_to_many = self.manager.get_many_to_many()
        result = self.manager.task3(many_to_many)

        # Проверяем структуру результата
        self.assertIsInstance(result, dict, "Результат должен быть словарем")

        # Проверяем, что в результатах только компьютеры, начинающиеся с 'A'
        for computer_name in result.keys():
            self.assertTrue(computer_name.startswith('A'),
                            f"Компьютер '{computer_name}' должен начинаться с 'A'")

        # Проверяем, что 'A Test Computer' есть в результатах
        self.assertIn('A Test Computer', result,
                      "Компьютер 'A Test Computer' должен быть в результатах")

        # Проверяем, что у 'A Test Computer' есть список моделей
        self.assertIsInstance(result['A Test Computer'], list,
                              "Значение должно быть списком моделей")

        # Проверяем конкретную модель (Intel Pentium)
        self.assertIn('Intel Pentium', result['A Test Computer'],
                      "Модель 'Intel Pentium' должна быть в списке")


if __name__ == '__main__':
    # Запуск модульных тестов
    unittest.main()