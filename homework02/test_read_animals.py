#!/usr/bin/env python3
import unittest
from read_animals import generate_id

class TestReadAnimals(unittest.TestCase):

    def test_generate_id(self):
        animal = dict()
        animal['head'] = 'raven'
        self.assertRaises(KeyError, generate_id, animal) # raises key error if missing attributes
        animal['body'] = 'cow-kit'
        animal['arms'] = 6
        animal['legs'] = 3
        self.assertEqual(generate_id(animal), 'vck0731') 
        animal['head'] = 'snake'
        animal['body'] = 'toucan-cicada'
        animal['arms'] = 10
        animal['legs'] = 12
        self.assertEqual(generate_id(animal), 'atc1354')
        self.assertRaises(AssertionError, generate_id, 'this is a string')
        self.assertRaises(AssertionError, generate_id, [0, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()
