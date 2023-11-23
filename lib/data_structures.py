spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food.get("name","")for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
       return [food for food in spicy_foods if food.get("heat_level", 0) > 5]
pass

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        heat_level = "🌶" * food.get("heat_level", 0)
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {heat_level}")
pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
       return next((food for food in spicy_foods if food.get("cuisine") == cuisine), None)
pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

    pass

def get_average_heat_level(spicy_foods):
     total_heat = sum(food.get("heat_level", 0) for food in spicy_foods)
     num_foods = len(spicy_foods)
     return total_heat // num_foods if num_foods > 0 else 0
pass

def create_spicy_food(spicy_foods, spicy_food):
     spicy_foods.append(spicy_food)
     return spicy_foods
pass
