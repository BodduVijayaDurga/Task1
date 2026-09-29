import streamlit as st


t1, t2 = st.tabs(["Login", "Register"])


with t1:

    st.title("Login Form")

    with st.form("Login Form"):

        st.text_input("Email", placeholder="Enter email here")

        st.text_input(
            "Password",
            placeholder="Enter password here",
            type="password"
        )

        st.selectbox("Role", ["", "trainer", "student"])

        st.form_submit_button("Login")


with t2:

    st.title("Registration Form")

    with st.form("Reg form"):

        st.text_input("Name", placeholder="Enter name here")

        st.text_input("Email", placeholder="Enter email here")

        st.text_input(
            "Password",
            placeholder="Enter password here",
            type="password"
        )

        st.text_input(
            "Confirm Password",
            placeholder="Re-enter password here",
            type="password"
        )

        st.selectbox("Role", ["", "trainer", "student"])

        st.form_submit_button("Register")