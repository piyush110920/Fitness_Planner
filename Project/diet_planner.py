import streamlit as st
import pandas as pd
import joblib

def diet_planner_app():
    # Load your trained model
    model = joblib.load('./diet_model3.pkl')

    FEATURE_NAMES = [
        'Gender', 'Age', 'Diabetes', 'Weight', 'Wanna Loose Weight', 'Height', 'BMI', 'Calories', 'Meal Type',
        'Exercise_Lightly Active', 'Exercise_Moderate', 'Exercise_Sedentary', 'Exercise_Super Active', 'Exercise_Very Active',
        'Workout_High intensity Exercise', 'Workout_Light Exercise', 'Workout_Moderate Exercise', 'Workout_Sedentary Lifestyle'
    ]

    DIET_NAME_MAPPING = {
        0: 'Balanced Diet',
        1: 'Energy boost diet',
        2: 'Light Activity Fuel',
        3: 'Fitness Diet'
    }

    recipes = {
        'Balanced Diet': {
            'breakfast': [
                'Oatmeal with Fruits and Nuts',
                'Greek Yogurt with Honey and Almonds',
                'Chia Pudding with Fresh Berries',
                'Smoothie with Spinach and Banana',
                'Whole Grain Toast with Avocado and Poached Egg',
                'Scrambled Eggs with Veggies',
                'Quinoa Porridge with Almond Milk'
            ],
            'lunch': [
                'Grilled Chicken with Steamed Vegetables',
                'Quinoa Salad with Lemon Dressing',
                'Vegetable Stir-fry with Brown Rice',
                'Lentil Soup with Whole Grain Bread',
                'Stuffed Bell Peppers with Ground Turkey',
                'Spinach and Mushroom Frittata',
                'Chicken Caesar Salad'
            ],
            'dinner': [
                'Baked Salmon with Asparagus',
                'Roasted Sweet Potatoes with Kale Salad',
                'Whole Wheat Pasta with Marinara Sauce',
                'Tofu and Broccoli Stir-fry',
                'Grilled Shrimp with Quinoa and Arugula Salad',
                'Stuffed Eggplant with Quinoa',
                'Zucchini Noodles with Pesto'
            ]
        },
        'Energy boost diet': {
            'breakfast': [
                'Peanut Butter Banana Smoothie',
                'Green Smoothie with Chia Seeds',
                'Protein-Packed Overnight Oats',
                'Energy Balls with Dates and Almonds',
                'Almond Butter Toast with Banana',
                'Hard-Boiled Eggs with Fruit',
                'Granola with Coconut Flakes'
            ],
            'lunch': [
                'Trail Mix with Nuts and Dried Fruits',
                'Omelette with Spinach and Avocado',
                'Quinoa and Black Bean Salad',
                'Greek Yogurt with Granola and Berries',
                'Tuna Salad with Whole Grain Crackers',
                'Edamame and Hummus Snack Plate',
                'Sweet Potato Fries with Guacamole'
            ],
            'dinner': [
                'Grilled Chicken with Avocado Salad',
                'Roasted Chickpeas with Spices',
                'Mango and Avocado Salad',
                'Nutty Granola with Berries',
                'Salmon with Asparagus',
                'Zoodles (Zucchini Noodles) with Pesto',
                'Cottage Cheese with Pineapple'
            ]
        },
            'Light Activity Fuel': {
            'breakfast': [
                'Whole Grain Toast with Almond Butter',
                'Greek Yogurt with Berries',
                'Avocado Smoothie with Almond Milk',
                'Scrambled Eggs with Spinach',
                'Cottage Cheese with Peaches',
                'Apple Slices with Peanut Butter',
                'Protein Pancakes with Fruit'
            ],
            'lunch': [
                'Chicken Salad with Olive Oil Dressing',
                'Turkey and Spinach Roll-Ups',
                'Chickpea Salad with Lemon Tahini',
                'Baked Falafel with Cucumber Yogurt',
                'Stuffed Portobello Mushrooms',
                'Spiced Lentils with Roasted Veggies',
                'Salmon with Sweet Potato'
            ],
            'dinner': [
                'Zucchini Noodles with Pesto',
                'Stuffed Eggplant with Spinach and Feta',
                'Roasted Beet and Goat Cheese Salad',
                'Miso Soup with Tofu',
                'Roasted Chicken with Vegetables',
                'Baked Eggplant with Tahini Sauce',
                'Grilled Shrimp with Brown Rice'
            ]
        },
        'Fitness Diet': {
            'breakfast': [
                'Protein Shake with Almond Milk',
                'Egg White Scramble with Veggies',
                'Omelette with Spinach and Tomatoes',
                'Protein Pancakes with Greek Yogurt',
                'Smoothie with Berries and Protein Powder',
                'Avocado and Egg on Whole Wheat Toast',
                'Cottage Cheese with Pineapple Chunks'
            ],
            'lunch': [
                'Turkey Sandwich with Whole Wheat Bread',
                'Quinoa Bowl with Black Beans and Salsa',
                'Stir-fried Vegetables with Tofu',
                'Grilled Chicken with Brown Rice',
                'Grilled Salmon with Couscous',
                'Chicken Salad with Olive Oil Dressing',
                'Baked Tilapia with Quinoa'
            ],
            'dinner': [
                'Roasted Chicken with Sweet Potatoes',
                'Steak and Mixed Veggie Stir-fry',
                'Turkey Meatballs with Zoodles',
                'Baked Chicken with Quinoa and Kale',
                'Grilled Salmon with Avocado Salad',
                'Stir-fried Tofu with Broccoli',
                'Stuffed Bell Peppers with Ground Turkey'
            ]
        }
    }

    st.title("Automatic Diet Plan Generator")

    st.write("Please fill in the details to generate your personalized diet plan.")

    age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=70.0)
    height = st.number_input("Enter your height (cm)", min_value=0.0, value=170.0)

    gender = st.radio("Gender", ('Male', 'Female'))
    gender = 0 if gender == 'Male' else 1

    bmi = weight / ((height / 100) ** 2)
    calories = st.number_input("Calories intake per day", min_value=1000, max_value=4000, value=2000)

    exercise = st.selectbox("Select your exercise level", ['Sedentary', 'Lightly Active', 'Moderate', 'Very Active', 'Super Active'])
    workout = st.selectbox("Select your workout intensity", ['Sedentary Lifestyle', 'Light Exercise', 'Moderate Exercise', 'High intensity Exercise'])

    if st.button("Generate Diet Plan"):
        input_data = {
            'Age': age,
            'Weight': weight,
            'Height': height,
            'Gender': gender,
            'BMI': bmi,
            'Calories': calories,
            f'Exercise_{exercise}': 1,
            f'Workout_{workout}': 1
        }

        input_df = pd.DataFrame([input_data])
        input_df = input_df.reindex(columns=FEATURE_NAMES, fill_value=0)

        predicted_key = model.predict(input_df)[0]
        recommended_diet = DIET_NAME_MAPPING.get(predicted_key)

        st.subheader("Your Recommended Diet Plan:")
        st.write(recommended_diet)

        recommended_recipes = recipes.get(recommended_diet)
        if recommended_recipes:
            breakfast_recipes = pd.DataFrame(recommended_recipes['breakfast'], columns=['Breakfast Recipes'])
            lunch_recipes = pd.DataFrame(recommended_recipes['lunch'], columns=['Lunch Recipes'])
            dinner_recipes = pd.DataFrame(recommended_recipes['dinner'], columns=['Dinner Recipes'])

            st.subheader("Breakfast Recipes:")
            st.table(breakfast_recipes)

            st.subheader("Lunch Recipes:")
            st.table(lunch_recipes)

            st.subheader("Dinner Recipes:")
            st.table(dinner_recipes)
        else:
            st.write("No recipes available for the predicted diet.")