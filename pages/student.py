import streamlit as st

def app():
    st.title("Student")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Initialize session states
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    if 'button_clicked' not in st.session_state:
        st.session_state.button_clicked = False

    # Function to handle button click
    def handle_button_click(answer):
        st.session_state.answers.append(answer)
        st.session_state.button_clicked = True

    # Check if a button was clicked
    if not st.session_state.button_clicked:
        # Display the title for the level of understanding
        st.subheader("Level of Understanding (tap once to chose and again to approve)")

        # Display the buttons and handle the button clicks
        col1, col2, col3, col4, col5 = st.columns(5)
        if col1.button("1"):
            handle_button_click(1)
        if col2.button("2"):
            handle_button_click(2)
        if col3.button("3"):
            handle_button_click(3)
        if col4.button("4"):
            handle_button_click(4)
        if col5.button("5"):
            handle_button_click(5)
    else:
        # Display the thank you message
        st.success("Thank you :)")
