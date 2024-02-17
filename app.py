import streamlit as st
from openai import OpenAI
import os
import requests

client = OpenAI(
   
    api_key= os.environ["openai_key"]
)

st.title('Fitness and Diet Recommendation Bot')

# User Inputs
age = st.number_input("Age", min_value=0, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (kgs)", min_value=0)
height = st.number_input("Height (cm)", min_value=0)
goal = st.selectbox("Fitness Goal", ["Weight Loss (not an exercise)", "Muscle Gain", "Maintain Health (not an exercise)"])
food_allergies = st.selectbox("Food Allergies", ["Sesame", "Peanut", "Gluten", "Soy"])
diet_restriction = st.selectbox("Diet Restriction", ["Vegetarian", "Paleo", "Vegan", "Lacto-Vegetarian"])
muscle = st.selectbox("Muscle Target Exercise", ["abdominals", "biceps", "glutes", "lats", "quadriceps"])
difficulty = st.selectbox("Difficulty Level", ["beginner", "intermediate", "expert"])


def fetch_nutrition_data(food_allergies, diet_restriction):
    API_ENDPOINT = "https://api.spoonacular.com/mealplanner/generate?timeFrame=day"
    params = {
        "intolerances": food_allergies,
        "diet": diet_restriction,        
        "apiKey": os.environ["nutri_key"]
    }
    headers = {"Authorization": os.environ["nutri_key"]}

    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        foods = response.json()
        return [exercise['title'] for exercise in foods.get('meals', [])]
    except requests.exceptions.JSONDecodeError:
        print("Received invalid JSON response")
        return []
    
def fetch_workout_data(muscle, difficulty):
    # Construct the API URL based on the given muscle and difficulty
    api_url = f'https://api.api-ninjas.com/v1/exercises?muscle={muscle}&difficulty={difficulty}'
    api_key = os.environ["workout_key"]
    
    # Make the GET request to the API
    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        exercises = response.json()

        # Get only the first two exercises using list slicing
        first_three_exercises = exercises[:3]

        # Iterate through the first three exercises and print their names
        for exercise in first_three_exercises:
            print(exercise['name'])
    else:
        # If the request was not successful, print the error
        print("Error:", response.status_code, response.text)


# Fetch data and construct prompt
nutrition = fetch_nutrition_data(food_allergies, diet_restriction)
workouts = fetch_workout_data(muscle, difficulty)

prompt = f"Given the age {age}, gender {gender}, weight {weight} and height {height}, considering the following workouts {workouts} and nutrition options {nutrition}, provide a personalized fitness and diet plan."



# Function to get recommendations
def get_recommendations(prompt):
        
    response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Assuming the response is structured with 'choices'
    if response.choices and len(response.choices) > 0:
        # Accessing the 'content' of the message in the first choice
        message_content = response.choices[0].message.content
        return message_content.strip()
    else:
        return "No response generated."
       

# Display recommendations
if st.button('Get Recommendations'):
    recommendations = get_recommendations(prompt)
    st.subheader("Recommendations")
    st.write(recommendations)

