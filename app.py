import streamlit as st

# Simpele gebruikersdatabase
USERS = {"admin": "1234", "gebruiker": "wachtwoord"}

# Sessiebeheer voor login-status
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Loginpagina
def login():
    st.title("Login")
    username = st.text_input("Gebruikersnaam")
    password = st.text_input("Wachtwoord", type="password")

    if st.button("Inloggen"):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Succesvol ingelogd! Je wordt doorgestuurd...")
            st.experimental_rerun()
        else:
            st.error("Ongeldige login")

# Hoofdapp na inloggen
def main_app():
    st.sidebar.title(f"Welkom, {st.session_state['username']}")
    st.title("Beveiligde Webapp")
    st.write("Je hebt succesvol ingelogd!")

    if st.button("Uitloggen"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

# Login check
if st.session_state["logged_in"]:
    main_app()
else:
    login()

