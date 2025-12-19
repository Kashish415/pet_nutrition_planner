# hardcoded data for pet nutrition planning
ACTIVITY_FACTORS = {
    "low": 1.1,
    "medium": 1.4,
    "high": 1.7
}

BASE_MULTIPLIER = {
    "dog": 1.2,
    "cat": 1.3
}

UNSAFE_FOODS = {
    "dog": ["chocolate", "grapes", "onions","sweets","alcohol"],
    "cat": ["garlic", "onions", "raw eggs", "raw fish", "yeast dough"]
}

def age_category(age):
    if age < 1:
        return "young"
    if age <= 7:
        return "adult"
    return "senior"


def weight_category(weight_kg):
    if weight_kg < 5:
        return "small"
    if weight_kg <= 20:
        return "medium"
    return "large"


# calorie calculation using standard RER-based formula
def estimate_calories(weight_kg, activity, pet_type):

    rer = 70 * (weight_kg ** 0.75)
    return round(rer * BASE_MULTIPLIER[pet_type] * ACTIVITY_FACTORS[activity])

# preparing LLM context
def build_pet_context(pet):

    return {
        "pet_type": pet["type"],
        "breed": pet["breed"],
        "age_years": pet["age"],
        "age_group": age_category(pet["age"]),
        "weight_kg": pet["weight"],
        "weight_category": weight_category(pet["weight"]),
        "activity_level": pet["activity"],
        "allergies": pet["allergies"],
        "baseline_calories": estimate_calories(
            pet["weight"], pet["activity"], pet["type"]
        ),
        "unsafe_foods": UNSAFE_FOODS.get(pet["type"], [])
    }