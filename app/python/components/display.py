import streamlit as st
import json

from dataclasses import dataclass, field
from components.chat import Chat

@dataclass
class Display:
    agent: Chat = field(default_factory = Chat)
    styles: str = field(default_factory=str)

    def __post_init__(self) -> None:
        self.agent = Chat()
        self.load_styles()

    def load_styles(self) -> None:
        with open('css/styles.css', 'r', encoding='utf-8') as styles:
            contents = styles.read()
            st.markdown(f'<style>{contents}</style>', unsafe_allow_html=True)

    def display_header(self, animation=False) -> None:
        """Displays the header for the application."""
        st.html('<div class="custom-h1"><div style="text-align: left;">Technology Applications TA!</div><div style="text-align: right;">2025</div></div>')
        if animation:
            self.box_loader = st.container(height=20, border=False)
            self.box_loader.markdown('<div class="moving-rainbow-circle"></div>', unsafe_allow_html=True)

    def display_sidebar(self) -> None:
        """Displays the sidebar for the application."""
        with st.sidebar:
            st.html('<div class="feedback">We are constantly developing on our appsite. Give us feedback via our chat or contact formula!</div>')

    def display_chat_interface(self) -> None:
        """Displays the chat interface for user-agent interaction."""
        chat_box = st.container(height=700, border=False)
        prompt = st.chat_input("Enter your message:")
        if prompt:
            self.process_user_input(prompt)
        self.display_chat(chat_box)

    def display_chat(self, chat_box) -> None:
        """Displays the chat messages in the chat box."""
        for message in st.session_state.messages:
            avatar = "🧑‍💻" if message["role"] == "user" else "🧑‍💼" 
            with chat_box.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

    def process_user_input(self, prompt: str) -> None:
        """Processes the user input from the chat, adding it to the conversation."""
        self.agent.context.add_message("user", prompt)
        self.agent.context.add_message("assistant", self.agent.run(prompt))
