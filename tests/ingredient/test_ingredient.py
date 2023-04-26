from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("queijo mussarela")
    lasanha = Ingredient("massa de lasanha")

    assert cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }

    assert lasanha.restrictions == {
        Restriction.LACTOSE,
        Restriction.GLUTEN
    }

    assert lasanha.name == "massa de lasanha"
    assert lasanha.__repr__() == f"Ingredient('{lasanha.name}')"
    assert lasanha.__repr__() != f"Ingredient('{cheese.name}')"

    assert cheese.name == "queijo mussarela"
    assert cheese.__repr__() == f"Ingredient('{cheese.name}')"
    assert lasanha.__repr__() != f"Ingredient('{cheese.name}')"

    assert lasanha.__hash__() != cheese.__hash__()
    assert lasanha.__hash__() == lasanha.__hash__()

    assert lasanha == lasanha
    assert cheese != lasanha
