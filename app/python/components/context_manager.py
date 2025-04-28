import streamlit as st
from dataclasses import dataclass

@dataclass
class ContextManager:

    def __post_init__(self) -> None:
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def add_message(self, role: str, message: str) -> None:
        """Adds a message to the context."""
        st.session_state.messages.append({"role": role, "content": message})

    def reset_chat(self) -> None:
        """Resets the chat history and other parameters."""
        st.session_state.messages = []

    def get_chat_context(self) -> str:
        """Retrieves the current context of the chat."""
        return "\n".join(message["content"] for message in st.session_state.messages[-6:])

