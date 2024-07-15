import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
    st.title("Teacher")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Initialize session states for answers tracking
    if 'answers' not in st.session_state:
        st.session_state.answers = []

    # Button to show the results
    if st.button("Show Results"):
        if st.session_state.answers:
            df = pd.DataFrame(st.session_state.answers, columns=['Answer'])

            # Plot the graph with custom colors
            fig, ax = plt.subplots()
            color_map = {1: '#FF9999', 2: '#FF4C4C', 3: '#FFA500', 4: '#90EE90', 5: '#32CD32'}
            colors = df['Answer'].map(color_map)
            df['Answer'].value_counts().sort_index().plot(kind='bar', ax=ax, color=colors)
            ax.set_xlabel("Level of Understanding")
            ax.set_ylabel("Number of Students")
            ax.set_title("Class Status of Understanding")
            plt.xticks(rotation=0)  # Ensure x-axis labels are horizontal

            st.pyplot(fig)

            # Calculate and display percentages
            total_responses = len(st.session_state.answers)
            percentages = df['Answer'].value_counts(normalize=True) * 100
            st.write("Percentages of each level of understanding:")
            for level in range(1, 6):
                st.write(f"Level {level}: {percentages.get(level, 0):.2f}%")
        else:
            st.write("No data to display yet.")

def app_with_password():
    st.title("Teacher")
    password = st.text_input("Enter password", type="password")
    if password == '1998':
        app()
    elif password:
        st.error("Incorrect password")
