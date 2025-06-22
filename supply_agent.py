from adk.agent import Agent

class SupplyAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def run(self, message):
        locations = message.get("rescue_locations", [])
        print(f"[SupplyAgent] Sending supplies to: {locations}")
        final_update = f"Supplies sent to {locations}"
        self.send("CommunicationAgent", {"final_update": final_update})
        return {"final_update": final_update}
