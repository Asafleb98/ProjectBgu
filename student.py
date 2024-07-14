import streamlit as st

# Initialize session states for answers tracking
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

# Function to handle button click
def handle_button_click(answer):
    st.session_state.answers.append(answer)
    st.session_state.button_clicked = True

# Right side (Student)
st.title("Student")
st.markdown("<hr>", unsafe_allow_html=True)

# Check if a button was clicked
if not st.session_state.button_clicked:
    # Display the title for the level of understanding
    st.subheader("Level of Understanding")

    # Display the buttons and handle the button clicks
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("1"):
            handle_button_click(1)
            st.success("Thank you :)")

    with col2:
        if st.button("2"):
            handle_button_click(2)
            st.success("Thank you :)")

    with col3:
        if st.button("3"):
            handle_button_click(3)
            st.success("Thank you :)")

    with col4:
        if st.button("4"):
            handle_button_click(4)
            st.success("Thank you :)")

    with col5:
        if st.button("5"):
            handle_button_click(5)
            st.success("Thank you :)")
