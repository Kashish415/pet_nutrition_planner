# Pet Nutrition Planner

## Overview

This project implements a nutrition recommendation system for pets. It takes basic pet details and generates a clear, explainable nutrition plan.
The goal is to show how structured logic and an AI model can work together to produce sensible output recommendations.

## Approach

This project uses a hybrid approach:

1. A rule-based system is used only to:

  - Categorize the pet (age group, weight category)
  - Estimate baseline daily calories 
  - Declare unsafe foods

2. A Large Language Model (Gemini) is then used to:

  - Reason over the structured information
  - Prioritize factors like age, activity level, weight and allergies
  - Resolve conflicts (for example: senior age but high activity)
  - Explain why a particular recommendation is made to the pet owner

## Workflow

1. The user enters pet details (type, breed, age, weight, activity, allergies).
2. Rule-based logic calculates baseline nutrition values. 
3. Structured pet context is passed to the LLM.
4. The LLM generates a concise and explainable nutrition recommendation.
5. The result is printed out in the terminal.

## Assumptions

1. Calorie estimation is based on a standard RER formula.
2. Recommendations are general and assistive in nature.

## Tools Used

- Python (version 3.9 or higher)
- Google Gemini (via google-genai)

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Install dependencies  
   `pip install -r requirements.txt`

4. Create your `.env` file. ( refer the `.env.example`)
   
   Add your Gemini API key

6. Run the project  
   `python main.py`
