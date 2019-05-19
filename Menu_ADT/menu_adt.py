import json
from Menu_ADT.linked_list.linked_list import LinkedList


class Menu:
    """
    ADT for food menu
    """

    def __init__(self, meals_file):
        """
        :param meals_file: json file
        """
        self.meals_file = meals_file

        with open(self.meals_file) as f:
            self._data = json.load(f)

        self._products = dict()
        self._instructions = dict()
        self._images = dict()

        # Call methods to fill dictionaries
        self.__find_products()
        self.__find_instructions()
        self.__find_image()

    def __find_products(self):
        """
        Fills _products dict with ingredients for each meal
        """
        for i in self._data.values():
            self._products[i['title']] = LinkedList()
            for j in i["extendedIngredients"]:
                self._products[i['title']].add(
                    (j['name'], j['measures']['metric']['amount'], j['measures']['metric']['unitShort']))
            self._products[i['title']].change_metric()

    def __find_instructions(self):
        """
        Fills _instructions dict with meal as a key and meal's preparing instructions as a value
        """
        for i in self._data.values():
            inst = [i["instructions"]] if [i["instructions"]] else ['']
            if inst[0]:
                if '\n' in inst[0]:
                    inst[0] = inst[0].replace('\n', '')
            self._instructions[i['title']] = inst

    def __find_image(self):
        """
        Fills _images dict with meal as a key and its image as a value
        """
        for i in self._data.values():
            self._images[i['title']] = i['image']

    def get_products(self):
        """
        :return: _products dict
        """
        return self._products

    def get_instructions(self):
        """
        :return: _instructions dict
        """
        return self._instructions

    def get_image(self):
        """
        :return: _image dict
        """
        return self._images
