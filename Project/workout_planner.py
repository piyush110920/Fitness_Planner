import pandas as pd
import streamlit as st

# Load the exercise data from the CSV file with error handling
try:
    exercises = pd.read_csv('cleaned_data.csv')

    # Ensure there are no NaN values in critical columns like 'Type', 'BodyPart', 'Equipment', and 'Level'
    exercises['Type'] = exercises['Type'].fillna('')
    exercises['BodyPart'] = exercises['BodyPart'].fillna('')
    exercises['Equipment'] = exercises['Equipment'].fillna('')
    exercises['Level'] = exercises['Level'].fillna('')
except FileNotFoundError:
    st.error("Error: The data file `cleaned_data.csv` was not found. Please upload the file and try again.")
    exercises = pd.DataFrame()  # Create an empty DataFrame to avoid errors

# Define a function to get dynamically filtered options for dropdowns
def get_filtered_options(df, column, filters):
    """Filter the dataset and return unique options for a column based on applied filters."""
    for col, value in filters.items():
        if value:  # Apply filter only if a value is selected
            df = df[df[col].str.contains(value, case=False, na=False)]
    return sorted(df[column].dropna().unique())

# Main logic in Streamlit
def mainq():
    #st.title("AI-Powered Exercise Recommendation")
    st.write("Get personalized exercise recommendations based on your fitness goals, body part, equipment, and level.")
    
    # Initialize user selection filters
    selected_filters = {
        'Type': '',
        'BodyPart': '',
        'Equipment': '',
        'Level': ''
    }
    
    # Step 1: Select fitness goal
    goal_options = get_filtered_options(exercises, 'Type', {})
    selected_filters['Type'] = st.selectbox("What's your main fitness goal?", ["Select an option"] + goal_options)
    if selected_filters['Type'] == "Select an option":
        selected_filters['Type'] = ''  # Reset to empty string if no valid selection

    # Step 2: Select body part
    body_part_options = get_filtered_options(exercises, 'BodyPart', {'Type': selected_filters['Type']})
    selected_filters['BodyPart'] = st.selectbox("What body part do you want to work on?", ["Select an option"] + body_part_options)
    if selected_filters['BodyPart'] == "Select an option":
        selected_filters['BodyPart'] = ''  # Reset to empty string if no valid selection

    # Step 3: Select equipment
    equipment_options = get_filtered_options(exercises, 'Equipment', {
        'Type': selected_filters['Type'],
        'BodyPart': selected_filters['BodyPart']
    })
    selected_filters['Equipment'] = st.selectbox("What equipment do you have?", ["Select an option"] + equipment_options)
    if selected_filters['Equipment'] == "Select an option":
        selected_filters['Equipment'] = ''  # Reset to empty string if no valid selection

    # Step 4: Select experience level
    level_options = get_filtered_options(exercises, 'Level', {
        'Type': selected_filters['Type'],
        'BodyPart': selected_filters['BodyPart'],
        'Equipment': selected_filters['Equipment']
    })
    selected_filters['Level'] = st.selectbox("What's your experience level?", ["Select an option"] + level_options)
    if selected_filters['Level'] == "Select an option":
        selected_filters['Level'] = ''  # Reset to empty string if no valid selection

    # Add a submit button
    if st.button('Submit'):
        # Filter the dataset based on all selected filters
        filtered_exercises = exercises.copy()
        for col, value in selected_filters.items():
            if value:
                filtered_exercises = filtered_exercises[filtered_exercises[col].str.contains(value, case=False, na=False)]

        # Display results
        if not filtered_exercises.empty:
            st.write("Here are some exercises that might be a good fit for you:")
            st.table(filtered_exercises[['Title', 'Desc']].head(50))  # Display in tabular format
        else:
            st.write("No exercises found matching your criteria. Try modifying your input.")

# Run the app
if __name__ == "__mainq__":
    mainq()