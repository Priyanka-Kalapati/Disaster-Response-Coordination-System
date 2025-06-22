from adk.agent import Agent

class LocationAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def run(self, message):
        zones = message.get("risk_zones", [])
        print(f"[LocationAgent] Mapping zones: {zones}")
        self.send("RescueAgent", {"locations": zones})
        return {"locations": zones}