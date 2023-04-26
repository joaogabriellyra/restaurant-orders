from csv import DictReader
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, encoding='utf-8') as file:
            menu = list(DictReader(file, delimiter=","))

        self.dishes = set()
        self.dishes_names = {}

        for snack in menu:
            plate = snack["dish"]
            if plate not in self.dishes_names:
                dish = Dish(plate, float(snack['price']))
                self.dishes.add(dish)
                self.dishes_names[plate] = dish
            else:
                dish = self.dishes_names[plate]
            dish.add_ingredient_dependency(
                Ingredient(snack["ingredient"]),
                int(snack["recipe_amount"])
            )
