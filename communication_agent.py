from adk.agent import Agent

class CommunicationAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def run(self, message):
        update = message.get("final_update", "No updates")
        print(f"[CommunicationAgent] Broadcasting: {update}")