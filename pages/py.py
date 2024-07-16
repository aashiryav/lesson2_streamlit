# Grade Calculator with Streamlit

import streamlit as st

# Initialize variables
grades = []
total_grades = 0
average = 0
grade_count = 0

# Title and description
st.title('Grade Calculator')
st.write('Enter five grades to calculate the average and letter grade.')

# Collect grades from user using Streamlit input
for _ in range(5):
    grade = st.number_input(f'Enter grade {_+1} (0-100):', min_value=0, max_value=100, key=_)
    if grade:
        grades.append(grade)
        total_grades += grade

# Calculate average if 5 grades are entered
if len(grades) == 5:
    average = total_grades / len(grades)

    # Determine letter grade using if, elif, else
    if 93 <= average <= 100:
        letter_grade = 'A'
    elif 90 <= average < 93:
        letter_grade = 'A-'
    # Add other conditions here...

    # Display the results
    st.write(f"Grades: {grades}")
    st.write(f"Average: {average:.2f}")
    st.write(f"Letter Grade: {letter_grade}")
else:
    st.write("Please enter all five grades.")

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
