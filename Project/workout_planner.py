import pandas as pd
import streamlit as st

# Load the exercise data from the CSV file with error handling
try:
    exercises = pd.read_csv('cleaned_data.csv')

    # Clean and standardize column names
    exercises.columns = exercises.columns.str.strip().str.title()  # Make first letter capital

    # Debug: Show the available columns
    st.write("Loaded columns:", exercises.columns.tolist())

    # Required columns for filtering and display
    required_cols = ['Type', 'Bodypart', 'Equipment', 'Level', 'Title', 'Desc']
    missing_cols = [col for col in required_cols if col not in exercises.columns]

    if missing_cols:
        st.error(f"Error: Missing required column(s): {', '.join(missing_cols)}")
        st.stop()

    # Fill NaN values in important columns
    for col in ['Type', 'Bodypart', 'Equipment', 'Level']:
        exercises[col] = exercises[col].fillna('')

except FileNotFoundError:
    st.error("Error: The data file `cleaned_data.csv` was not found. Please upload the file and try again.")
    exercises = pd.DataFrame()
    st.stop()

# Utility function to get filtered dropdown options
def get_filtered_options(df, column, filters):
    for col, value in filters.items():
        if value:
            df = df[df[col].str.contains(value, case=False, na=False)]
    return sorted(df[column].dropna().unique())

# Main Streamlit logic
def mainq():
    st.title("💪 AI-Powered Exercise Recommendation")
    st.write("Get personalized exercise recommendations based on your fitness goals, body part, equipment, and level.")

    selected_filters = {
        'Type': '',
        'Bodypart': '',
        'Equipment': '',
        'Level': ''
    }

    # Step 1: Select fitness goal
    goal_options = get_filtered_options(exercises, 'Type', {})
    selected_filters['Type'] = st.selectbox("What's your main fitness goal?", ["Select an option"] + goal_options)
    if selected_filters['Type'] == "Select an option":
        selected_filters['Type'] = ''

    # Step 2: Select body part
    body_part_options = get_filtered_options(exercises, 'Bodypart', {'Type': selected_filters['Type']})
    selected_filters['Bodypart'] = st.selectbox("What body part do you want to work on?", ["Select an option"] + body_part_options)
    if selected_filters['Bodypart'] == "Select an option":
        selected_filters['Bodypart'] = ''

    # Step 3: Select equipment
    equipment_options = get_filtered_options(exercises, 'Equipment', {
        'Type': selected_filters['Type'],
        'Bodypart': selected_filters['Bodypart']
    })
    selected_filters['Equipment'] = st.selectbox("What equipment do you have?", ["Select an option"] + equipment_options)
    if selected_filters['Equipment'] == "Select an option":
        selected_filters['Equipment'] = ''

    # Step 4: Select experience level
    level_options = get_filtered_options(exercises, 'Level', {
        'Type': selected_filters['Type'],
        'Bodypart': selected_filters['Bodypart'],
        'Equipment': selected_filters['Equipment']
    })
    selected_filters['Level'] = st.selectbox("What's your experience level?", ["Select an option"] + level_options)
    if selected_filters['Level'] == "Select an option":
        selected_filters['Level'] = ''

    # Submit button logic
    if st.button('Submit'):
        filtered_exercises = exercises.copy()
        for col, value in selected_filters.items():
            if value:
                filtered_exercises = filtered_exercises[filtered_exercises[col].str.contains(value, case=False, na=False)]

        # Show results
        if not filtered_exercises.empty:
            st.success("✅ Exercises found for your preferences:")
            st.table(filtered_exercises[['Title', 'Desc']].head(50))
        else:
            st.warning("⚠️ No exercises found matching your criteria. Try different options.")

# Run the Streamlit app
if __name__ == "__main__":
    mainq()
