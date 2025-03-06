import streamlit as st

# Simpele gebruikersdatabase met rollen
USERS = {
    "admin": {"password": "1234", "role": "admin"},
    "gebruiker": {"password": "wachtwoord", "role": "user"},
    "test": {"password": "test123", "role": "test"}  # Nieuwe testgebruiker
}

# Sessiebeheer voor login-status
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["role"] = None

# Loginpagina
def login():
    st.title("Login")
    username = st.text_input("Gebruikersnaam")
    password = st.text_input("Wachtwoord", type="password")

    if st.button("Inloggen"):
        if username in USERS and USERS[username]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = USERS[username]["role"]
            st.success(f"Succesvol ingelogd als {username} ({st.session_state['role']})")
            st.rerun()
        else:
            st.error("Ongeldige login")

# Hoofdapp met rolgebaseerde toegang
def main_app():
    st.sidebar.title(f"Welkom, {st.session_state['username']} ({st.session_state['role']})")
    st.title("Beveiligde Webapp")

    if st.session_state["role"] == "admin":
        st.subheader("Admin Dashboard")
        st.write("Je hebt volledige toegang tot de applicatie.")
        st.button("Beheer instellingen")
        st.button("Gebruikers beheren")

    elif st.session_state["role"] == "user":
        st.subheader("Gebruikers Dashboard")
        st.write("Welkom gebruiker, je hebt beperkte toegang.")

    elif st.session_state["role"] == "test":
        st.subheader("Testgebruiker")
        st.write("Je hebt beperkte rechten en kunt alleen deze pagina bekijken.")

    if st.button("Uitloggen"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = None
        st.session_state["role"] = None
        st.rerun()

# Login check
if st.session_state["logged_in"]:
    main_app()
else:
    login()
