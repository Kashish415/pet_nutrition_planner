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
def calculate_daily_calories(weight_kg, activity_level, pet_type):
    rer = 70 * (weight_kg ** 0.75)
    return rer * BASE_MULTIPLIER[pet_type] * ACTIVITY_FACTORS[activity_level]


def suggest_meal_type(pet_type, age, activity, weight_cat, has_allergies):

    if has_allergies:
        return "Home-cooked or hypoallergenic packaged food"

    age_group = age_category(age)

    if pet_type == "dog":

        if age_group == "young":
            return "Puppy food"

        if age_group == "senior":
            return "Easily digestible food with controlled calories"

        if activity == "high":
            return "Protein-rich packaged food or mixed diet"

        if activity == "low" and weight_cat in ["medium", "large"]:
            return "Calorie-controlled mixed diet"

        return "Balanced mixed diet"

    if pet_type == "cat":

        if age_group == "young":
            return "High-protein kitten food"

        if age_group == "senior":
            return "Easily digestible, high-protein food for senior cats"

        return "High-protein packaged food or mixed diet"


def feeding_frequency(pet_type, age):
    if age < 1:     # puppies/kittens -> 3 times, else 2 times
        return 3
    return 2


def portion_guidance(daily_calories, meals_per_day, activity):

    calories_per_meal = daily_calories / meals_per_day

    if activity == "low":
        note = "Avoid overfeeding."
    elif activity == "high":
        note = "Ensure adequate energy intake."
    else:
        note = "Maintain a consistent routine."

    return f"{meals_per_day} meals per day, ~{round(calories_per_meal)} calories per meal. {note}"


def foods_to_avoid(pet_type):
    return UNSAFE_FOODS.get(pet_type, [])

def get_user_input():
    return {
        "type": input("Pet type (dog/cat): ").strip().lower(),
        "breed": input("Breed: ").strip(),
        "age": float(input("Age (in years): ")),
        "weight": float(input("Weight (in kg): ")),
        "activity": input("Activity level (low/medium/high): ").strip().lower(),
        "allergies": input("Allergies (comma separated, leave blank if none): ").strip()
    }


def generate_nutrition_plan(pet):
    age_group = age_category(pet["age"])
    weight_cat = weight_category(pet["weight"])

    daily_calories = calculate_daily_calories(
        pet["weight"], pet["activity"], pet["type"]
    )

    meal_type = suggest_meal_type(
        pet["type"],
        pet["age"],
        pet["activity"],
        weight_cat,
        bool(pet["allergies"])
    )

    meals = feeding_frequency(pet["type"], pet["age"])

    return {
        "Pet Type": pet["type"],
        "Breed": pet["breed"],
        "Age Category": age_group,
        "Weight Category": weight_cat,
        "Estimated Daily Calories": round(daily_calories),
        "Suggested Meal Type": meal_type,
        "Portion Guidance": portion_guidance(daily_calories, meals, pet["activity"]),
        "Foods to Avoid": foods_to_avoid(pet["type"]),
        "Disclaimer": "General guidance only. Not a replacement for vet advice."
    }

if __name__ == "__main__":
    pet = get_user_input()
    plan = generate_nutrition_plan(pet)

    print("\n--- Pet Nutrition Recommendation ---")
    for x, y in plan.items():
        print(f"{x}: {y}")