# Pet Nutrition Planner

## Overview
<<<<<<< HEAD
This project implements a pet nutrition recommendation system. 

## Approach

- Rule-based logic is used only to prepare structured context
  (age group, weight category, baseline calories, unsafe foods).
- An LLM (Gemini) reasons over this context to:
  - Handle conflicting inputs
  - Prioritize factors like age, activity, and allergies
  - Explain why a particular recommendation is made
=======
This project is a simple, rule-based system that generates pet nutrition recommendations based on basic pet information and functional logic.  

## Approach

**Rule-based approach**

Each recommendation is derived from clearly defined rules based on:
- Pet type
- Age category
- Weight category
- Activity level
- Presence of allergies

## Calorie Estimation Logic
Daily calorie needs are estimated using a standard Resting Energy Requirement (RER) based formula:

RER = 70 × (weight in kg ^ 0.75)

This value is then adjusted using:
- Pet-type multiplier (dog / cat)
- Activity-level factor (low / medium / high)

## Inputs
The system accepts the following inputs:
- Pet type (dog or cat)
- Breed
- Age (in years)
- Weight (in kg)
- Activity level (low / medium / high)
- Allergies (optional)

## Outputs
The system generates:
- Estimated daily calorie requirement
- SuggestS meal type (home food / packaged / mixed)
- Feeding frequency and portion size guidance
- Foods or ingredients to avoid

The output is displayed directly in the terminal as a structured nutrition plan.

## Assumptions
- The pet does not have any serious medical conditions.
- Recommendations are general and based on common pet nutrition guidelines.
- The rules are purely heuristic-based and not learned from real-world datasets.
>>>>>>> f9316832d25c9ac1debdb23ee7a03cc77be816df


## How to Run
1. Clone the repository
2. Navigate to the project folder
<<<<<<< HEAD
3. Install dependencies  
   `pip install -r requirements.txt`

4. Create your `.env` file. ( refer the `.env.example`)
   Add your Gemini API key

5. Run the project  
   `python main.py`
=======
3. Run the script:

```bash
python planner.py
>>>>>>> f9316832d25c9ac1debdb23ee7a03cc77be816df
