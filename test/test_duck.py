import unittest
from app.duck import Duck, Flywithwings, MallardDuck, RubberDuck

class TestDucks(unittest.TestCase):
    """""Testing Duck Class"""
    
    def test_duck_display(self):
        with self.assertRaises(TypeError):
            duck = Duck()

    def test_duck_type_mallard(self):
        duck = MallardDuck()
        result  = duck.display()
        self.assertEqual(result, "I am a Mallard duck")

    def test_duck_type_mallard_fly(self):
        duck = MallardDuck()
        result  = duck.perform_fly()
        self.assertEqual(result, "I can fly")
    
    def test_rubber_duck(self):
        duck = RubberDuck()
        result  = duck.display()
        self.assertEqual(result, "I am a rubber duck")
        no_fly = duck.perform_fly()
        self.assertEqual(no_fly, "I cannot fly")

    def test_change_behaviour(self):
        duck = RubberDuck()
        result  = duck.display()
        self.assertEqual(result, "I am a rubber duck")
        no_fly = duck.perform_fly()
        self.assertEqual(no_fly, "I cannot fly")
        duck.set_fly_behaviour(Flywithwings)
        changed_behaviour = duck.perform_fly()
        self.assertEqual(changed_behaviour, "I can fly")