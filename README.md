# Pet Nutrition Planner

## Overview

This project implements a nutrition recommendation system for pets.

## Approach

- Rule-based logic is used only to prepare structured context
  (age group, weight category, baseline calories, unsafe foods).
- An LLM (Gemini) reasons over this context to:
  - Handle conflicting inputs
  - Prioritize factors like age, activity, and allergies
  - Explain why a particular recommendation is made

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Install dependencies  
   `pip install -r requirements.txt`

4. Create your `.env` file. ( refer the `.env.example`)
   
   Add your Gemini API key

6. Run the project  
   `python main.py`
