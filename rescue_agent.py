from adk.agent import Agent

class RescueAgent(Agent):
    def __init__(self, name):
        super().__init__(name)

    def run(self, message):
        locations = message.get("locations", [])
        print(f"[RescueAgent] Deploying rescue teams to: {locations}")
        self.send("SupplyAgent", {"rescue_locations": locations})
        return {"rescue_locations": locations}