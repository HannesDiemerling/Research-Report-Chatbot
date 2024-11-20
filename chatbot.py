# chatbot.py

import os
from dotenv import load_dotenv

from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentType, initialize_agent, Tool
from langchain_openai.chat_models import ChatOpenAI

# Agenten
from agents.research_report_agent import ResearchReportAgent
from agents.mpib_website_agent import MPIBWebsiteAgent
from agents.person_agent import PersonnelAgent
from agents.publications_agent import PublicationsAgent
from agents.organigram_agent import OrganigramAgent
from dotenv import load_dotenv

# Load .env
load_dotenv()

# main script for interacting with user and coordinating the agents

class MPIBChatbot:
    def __init__(self):
        # Check openai key
        self.llm = ChatOpenAI(temperature=0)
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # Initialise agents
        self.agents = {
            'ResearchReportAgent': ResearchReportAgent(),
            'MPIBWebsiteAgent': MPIBWebsiteAgent(),
            'PersonnelAgent': PersonnelAgent(),
            'PublicationsAgent': PublicationsAgent(),
            'OrganigramAgent': OrganigramAgent(),
        }

        # Define agents as tools
        self.tools = [
            Tool(
                name="Research Report Tool",
                func=self.agents['ResearchReportAgent'].execute,
                description="Nützlich für Fragen zum Forschungsbericht 2023-2026."
            ),
            Tool(
                name="MPIB Website Tool",
                func=self.agents['MPIBWebsiteAgent'].execute,
                description="Nützlich für allgemeine Informationen über das MPIB."
            ),
            Tool(
                name="Personnel Tool",
                func=self.agents['PersonnelAgent'].execute,
                description="Nützlich für Informationen über Mitarbeiter des MPIB."
            ),
            Tool(
                name="Publications Tool",
                func=self.agents['PublicationsAgent'].execute,
                description="Nützlich für Informationen über Publikationen des MPIB."
            ),
            Tool(
                name="Organigram Tool",
                func=self.agents['OrganigramAgent'].execute,
                description="Nützlich für Fragen zur Organisationsstruktur des MPIB."
            ),
        ]

        # Initialise agent chain
        self.agent_chain = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory,
        )

    def generate_response(self, user_input: str) -> str:
        response = self.agent_chain.run(input=user_input)
        return response