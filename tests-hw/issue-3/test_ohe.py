"""Tests for One Hot Encoder fit_transform."""
from one_hot_encoder import fit_transform
import unittest
import random


class TestOHEFitTransfom(unittest.TestCase):
    """Tests for One Hot Encoder fit_transform."""

    def test_basics(self):
        """Basic test."""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertIsInstance(transformed_cities, list)
        self.assertIsInstance(transformed_cities[0][0], str)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_len_random(self):
        """Test result len using random values."""
        values = []
        rnd_len = random.randint(0, 1e3)
        for _ in range(rnd_len):
            values.append(str(random.randint(0, 1e3)))
        transformed_values = fit_transform(values)
        unique_keys = {el[0] for el in transformed_values}
        self.assertEqual(len(unique_keys), len(set(values)))

    def test_multi_arg(self):
        """Test multiargument functionality."""
        sex_labels = ['male', 'female']
        exp_transformed_sex_labels = [
            ('male', [0, 1]),
            ('female', [1, 0]),
        ]
        transformed_sex_labels = fit_transform(*sex_labels)
        self.assertEqual(transformed_sex_labels, exp_transformed_sex_labels)

    def test_type_error(self):
        """Test taht TypeError raised."""
        with self.assertRaises(TypeError):
            fit_transform(42)

        with self.assertRaises(TypeError):
            fit_transform(42, 21)


if __name__ == '__main__':
    unittest.main()
