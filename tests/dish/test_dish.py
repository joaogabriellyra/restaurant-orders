from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_of_cheese = Dish("cheese", 8.5)
    dish_of_barbecue = Dish("meet", 22.5)
    cheese = Ingredient("queijo mussarela")
    meet = Ingredient("carne")

    dish_of_cheese.add_ingredient_dependency(cheese, 2)
    dish_of_barbecue.add_ingredient_dependency(meet, 5)

    assert dish_of_cheese.name == "cheese"
    assert dish_of_cheese.__hash__() == dish_of_cheese.__hash__()
    assert dish_of_barbecue.__hash__() != dish_of_cheese.__hash__()
    assert dish_of_cheese == dish_of_cheese
    assert dish_of_cheese != dish_of_barbecue
    assert dish_of_cheese.__repr__() == "Dish('cheese', R$8.50)"
    assert dish_of_cheese.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert dish_of_cheese.get_ingredients() == {Ingredient('queijo mussarela')}
    with pytest.raises(TypeError):
        Dish("café", "1")
    with pytest.raises(ValueError):
        Dish("café", -1)
