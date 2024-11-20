from abc import ABC, abstractmethod

# default agent

class BaseAgent(ABC):
    @abstractmethod
    def execute(self, query):
        pass