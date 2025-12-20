from planner import build_pet_context
from llm import run_llm_reasoning
import time

def get_user_input():
    return {
        "type": input("Pet type (dog/cat): ").strip().lower(),
        "breed": input("Breed: ").strip(),
        "age": float(input("Age (in years): ")),
        "weight": float(input("Weight (in kg): ")),
        "activity": input("Activity level (low/medium/high): ").strip().lower(),
        "allergies": input("Allergies (comma separated, leave blank if none): ").strip()
    }


if __name__ == "__main__":
    pet = get_user_input()

    print("\nCollecting pet details...")
    time.sleep(0.6)

    print("Calculating baseline nutrition needs...")
    pet_context = build_pet_context(pet)     # from planner.py
    time.sleep(0.6)

    print("Generating final recommendations...\n")

    result = run_llm_reasoning(pet_context)
    print(result)
