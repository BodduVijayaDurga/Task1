import streamlit as st 



def login_status_check():
    if not st.session_state.get("status",False):
        st.title("login first")
        st.switch_page("app.py")
    



def role_check():
    if st.session_state.get("role","") != "student"  : 
        st.title("access denied")
        st.switch_page("app.py")


login_status_check()
role_check()


st.title("student dashboard")
