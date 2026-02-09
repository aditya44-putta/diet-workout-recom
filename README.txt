************* RECORDED VIDEO LINKS *************

1) Chatbot app demo and code explanation link --> https://www.loom.com/share/d1d8013a7d224512bfe80227b36c46fd

2) Setting up CI/CD pipeline for chatbot app full demo link --> https://www.loom.com/share/369c5bb686ba4a5b96a4ca29c573a335

3) 3) AWS CI CD setup for chatbot app full demo link --> https://www.loom.com/share/50563f050ea641db9704ba202fab6795

************************************************

Important Notice:
******
It is important you press Enter after inputting data in each field within the Streamlit UI; otherwise, the recommendations may not update correctly.
******

Diet and Workout Recommendation App:
This application is built with Streamlit and integrates various APIs including OpenAI, Nutrition (https://spoonacular.com/food-api/docs#Generate-Meal-Plan), and Workout (https://api-ninjas.com/api/exercises) APIs to deliver a customized recommendations.

***** It is adviced to get the API keys only from the below mentioned links for this app *****

1) Process to get the API keys and fill them in the app.py code:
	We get free API keys only after registering in the website.
	
	i) To get openai api key --> https://platform.openai.com/api-keys 
		and fill it in the app.py file line 7
	ii) To get nutrition data api key --> https://spoonacular.com/food-api/docs#Generate-Meal-Plan
		and fill it in the app.py file line 33, 37
	iii) To get the workout data API key --> https://api-ninjas.com/profile
		and fill it in the app.py file line 52

2) Clone this repository in your system 

3) Open command prompt get to the root folder of the app code & run the below commands

4) conda create -n diet_bot python=3.11.5

5) conda activate diet_bot

6) pip install --upgrade pip

7) pip install -r requirements.txt

8) streamlit run app.py
 


	
