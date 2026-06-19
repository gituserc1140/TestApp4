import streamlit as st

def main():
    """
    Main function to run the Streamlit application.
    """
    try:
        st.write("Hello World")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
