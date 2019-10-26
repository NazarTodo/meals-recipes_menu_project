# Meals and recipes menu project

Project by Nazar Pasternak and Nazar Todoshchuk for unviersity coursework.

Web-application, that helps create personal menu.

## Description

Our project lets any user with their own preferences create menu for a week and track the costs of each meal in order to save money.
We use an algorithm that chooses the best priced products for their value.


## Input and output

Program is built in such way that user chooses their most liked products and the ones that they do not want to have in their meals. 

The output is a menu and costs required for each meal.

## Program modules description

* `main.py` - main module, lets you run the program.
* `spoonacular.py` and `tesco.py` - API modules, that get info and write it to the json files.
  * `find_recipes(ing)` - function in `spoonacular.py`. Makes json file with info about recipes got from given ingredients.
  * `find_price(int)` - function in `tesco.py`. Makes a json file of a certain product request and writes it down.
* `menu_adt.py` - ADT module, using class LinkedList: `linkedlist.py`, that is based on Node and TwoWayNode classes.
  * Class `Menu`. Methods __find_products/_intructions/_image - fills dicts self._products/_intstructions/_images with meal as a key and relative info as value.
  * Class `LinkedList`. Basic two way linked list based on `TwoWayNode`. Has one additional method `change_metric`, for used for Menu ADT.
* `product_price.py` - module, that extracts information from json files and puts it into dictionary.
  * Function `price_product`. Returns price of a product based on json file with that product's info.
* `ADT_Example`, `API_Example`, `handling_data_example` - directories with modules and module, made to show an example of functions and methods used while executing main program.
* `test_menu.py` - Module with unittests for Menu ADT.
* `flask` - Directory that includes all front-end parts of the project and flask.

## Usage

Visit our website: http://pastor.pythonanywhere.com. (Currently unavailable due to lack of funds to pay for the API)

Follow given steps to create your own unique menu.

You also might clone this repository directly to your computer:
```
git clone https://github.com/NazarTodo/meals-recipes_menu_project.git
```
If you considered using program from your computer, here are the steps to follow:
1. Make sure you have installed all additional modules and libraries used in this program.(Flask)
1. Run `flask_c.py` module, which is in flask directory.


**_BEWARE_, that the program can only be ran from flask_c.py module. Runnung main.py module will not get you the expected result since the project is based on web-application. Main version of the program is on website: http://pastor.pythonanywhere.com.**

## Program test exmaples

Input : 
* beef
* tomato
* potato

After proceding, program output is:
* Super Stuffed Potatoes: £1.88
* Simple Mulligan Stew: £6.84
* Ranch-Style Steak Kabobs: £11.15

## Contribution

Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes
 

