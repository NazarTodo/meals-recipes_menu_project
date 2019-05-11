from unittest import TestCase
from menu_adt import Menu
from linkedlist import LinkedList


class TestMenu(TestCase):
    def setUp(self):
        self.menu = Menu('test_data.json')

    def test_get_product(self):
        self.assertEqual(str(self.menu.get_products()['Sheet Pan Home Fries']),
                         "[('baby potatoes', 0.56699, 'kg'), ('carrots', 2.0, ''), ('extra virgin olive oil', 1.5, ''), ('green bell pepper', 1.0, ''), ('kosher salt', 1.25, ''), ('onion', 1.0, ''), ('pepper', 4.0, ''), ]")
        self.assertTrue(isinstance(self.menu.get_products()['Sheet Pan Home Fries'], LinkedList))

    def test_get_instructions(self):
        self.assertTrue(isinstance(self.menu.get_instructions(), dict))
        self.assertEqual(str(self.menu.get_instructions()['Sheet Pan Home Fries']),
                         "['Preheat oven to 375F. Line a sheet pan with nonstick foil or spray with oil.Combine all the ingredients in a large bowl and toss well. Transfer to the sheet pan and spread in a single layer. Roast in the bottom rack 15 minutes. Turn and roast an additional 25 to 30 minutes, or until golden brown and cooked through.', [129.1]]")

    def test_get_images(self):
        self.assertTrue(isinstance(self.menu.get_image(), dict))
        self.assertEqual(str(self.menu.get_image()["Sheet Pan Home Fries"]),
                         'https://spoonacular.com/recipeImages/867150-556x370.jpg')
