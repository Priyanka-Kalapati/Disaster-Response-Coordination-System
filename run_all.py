from agents.data_analysis_agent import DataAnalysisAgent
from agents.location_agent import LocationAgent
from agents.rescue_agent import RescueAgent
from agents.supply_agent import SupplyAgent
from agents.communication_agent import CommunicationAgent

def main():
    print("===== STARTING MAIN FUNCTION =====")

    data_agent = DataAnalysisAgent("DataAnalysisAgent")
    location_agent = LocationAgent("LocationAgent")
    rescue_agent = RescueAgent("RescueAgent")
    supply_agent = SupplyAgent("SupplyAgent")
    comm_agent = CommunicationAgent("CommunicationAgent")

    print("===== Running Data Analysis Agent =====")
    risk_message = data_agent.run()
    print("Data Analysis Output:", risk_message)

    print("\n===== Running Location Agent =====")
    location_message = location_agent.run(risk_message)
    print("Location Agent Output:", location_message)

    print("\n===== Running Rescue Agent =====")
    rescue_message = rescue_agent.run(location_message)
    print("Rescue Agent Output:", rescue_message)

    print("\n===== Running Supply Agent =====")
    supply_message = supply_agent.run(rescue_message)
    print("Supply Agent Output:", supply_message)

    print("\n===== Running Communication Agent =====")
    comm_agent.run(supply_message)

    print("\n===== All Agents Ran Successfully! =====")

if __name__ == "__main__":
    main()
