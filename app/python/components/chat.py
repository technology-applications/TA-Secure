import os
import streamlit as st
from dataclasses import dataclass, field
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate
from components.context_manager import ContextManager

@dataclass
class Chat:
    """Die Chat-Klasse verwaltet die Interaktion mit dem Chatbot und verarbeitet Benutzereingaben."""
    template: str = field(default_factory=str)
    context: ContextManager = field(init=False)
    llm: OllamaLLM = field(init=False)
    prompt: PromptTemplate = field(init=False)

    def __post_init__(self):
        with open('txt/template.txt', 'r') as file:
            self.template = file.read()
        self.context = ContextManager()
        self.llm  = OllamaLLM(model='llama3.1', base_url='http://ollama:11434')
        self.prompt = PromptTemplate(template=self.template, input_variables=["user_prompt", "chat_history"])
        self.chain = self.prompt | self.llm

    def run(self, user_prompt: str) -> str:
        """Executes the chat model with the given user prompt."""
        response = self.chain.invoke({
            "user_prompt": user_prompt,
            "chat_history": self.context.get_chat_context(),
        })
        return response
