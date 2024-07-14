import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import xlsxwriter

# Define the layout with a white line separator
col1, col_divider, col2 = st.columns([1, 0.05, 1])

# Initialize session states for answers tracking and result display
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'show_results' not in st.session_state:
    st.session_state.show_results = False

# Function to export data to Excel with percentages and graph
def export_to_excel_with_graph(data, percentages):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    workbook = writer.book
    worksheet = workbook.add_worksheet('Results')
    writer.sheets['Results'] = worksheet

    # Write percentages
    worksheet.write('A1', 'Level of Understanding')
    worksheet.write('B1', 'Percentage')
    for idx, level in enumerate(percentages.index, start=1):
        worksheet.write(idx, 0, level)
        worksheet.write(idx, 1, percentages[level])

    # Create a bar chart
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({
        'categories': ['Results', 1, 0, len(percentages), 0],
        'values': ['Results', 1, 1, len(percentages), 1],
        'fill': {'color': '#FF9999'},
    })

    chart.set_title({'name': 'Class Status of Understanding'})
    chart.set_x_axis({'name': 'Level of Understanding'})
    chart.set_y_axis({'name': 'Percentage'})

    worksheet.insert_chart('D2', chart)

    writer.close()
    processed_data = output.getvalue()
    return processed_data

# Left side (Teacher)
with col1:
    st.title("Teacher")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Button to show/hide class status of understanding
    if st.button("Show Results"):
        st.session_state.show_results = True

    if st.button("Hide Results"):
        st.session_state.show_results = False

    # Show graph and percentages if results are displayed
    if st.session_state.show_results and st.session_state.answers:
        df = pd.DataFrame(st.session_state.answers, columns=['Answer'])
        
        # Plot the graph with custom colors
        fig, ax = plt.subplots()
        color_map = {1: '#FF9999', 2: '#FF4C4C', 3: '#FFA500', 4: '#90EE90', 5: '#32CD32'}
        colors = df['Answer'].map(color_map)
        df['Answer'].value_counts().sort_index().plot(kind='bar', ax=ax, color=colors)
        ax.set_xlabel("Level of Understanding")
        ax.set_ylabel("Number of Students")
        ax.set_title("Class Status of Understanding")
        st.pyplot(fig)

        # Calculate and display percentages
        total_responses = len(st.session_state.answers)
        percentages = df['Answer'].value_counts(normalize=True) * 100
        st.write("Percentages of each level of understanding:")
        for level in range(1, 6):
            st.write(f"Level {level}: {percentages.get(level, 0):.2f}%")

        # Button to export data to Excel
        if st.button("Export to Excel"):
            excel_data = export_to_excel_with_graph(df, percentages)
            st.download_button(label='Download Excel file',
                               data=excel_data,
                               file_name='class_status_of_understanding.xlsx',
                               mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    elif st.session_state.show_results:
        st.write("No data to display yet.")

# White line separator
with col_divider:
    st.markdown(
        """
        <style>
        .divider {
            height: 100%;
            width: 2px;
            background-color: white;
            margin: auto;
        }
        </style>
        <div class="divider"></div>
        """,
        unsafe_allow_html=True,
    )

# Right side (Student)
with col2:
    st.title("Student")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Initialize session states
    if 'quiz_number' not in st.session_state:
        st.session_state.quiz_number = 1
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    # Function to handle button click
    def handle_button_click(answer):
        st.session_state.answers.append(answer)
        st.session_state.quiz_number += 1
        st.session_state.button_clicked = True

    # Display the second title with the quiz number
    st.subheader(f"Student Number: {st.session_state.quiz_number}")

    # Display the buttons and handle the button clicks
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("1"):
            handle_button_click(1)
    with col2:
        if st.button("2"):
            handle_button_click(2)
    with col3:
        if st.button("3"):
            handle_button_click(3)
    with col4:
        if st.button("4"):
            handle_button_click(4)
    with col5:
        if st.button("5"):
            handle_button_click(5)
