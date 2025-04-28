import streamlit as st
from components.display import Display

def main():
    st.set_page_config(
        page_title="TA!",
        layout="wide")

    display = Display()
    display.display_header(animation=True)

    col1, col2, col3 = st.columns([1,3,1], gap="large", vertical_alignment="top")
    with col1:
        pass
    with col2:
        display.display_chat_interface()
    with col3:
        pass

if __name__ == '__main__':
    main()
