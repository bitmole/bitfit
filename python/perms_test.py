import perms
import unittest

class KnownValues(unittest.TestCase):
    cat_permutations = {
        'cat',
        'cta',
        'act',
        'atc',
        'tca',
        'tac',
    }

    def test_permuntations(self):
        result = perms.permute('cat')
        self.assertEqual(set(result), self.cat_permutations)

if __name__ == "__main__":
    unittest.main()
