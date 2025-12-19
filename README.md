# Pet Nutrition Planner

## Overview
This project is a simple, rule-based system that generates pet nutrition recommendationS based on basic pet information and functional logic.  

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


## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run the script:

```bash
python planner.py
