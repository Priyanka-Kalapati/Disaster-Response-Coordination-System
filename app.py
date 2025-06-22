from flask import Flask, jsonify
from flask_cors import CORS   # ✅ Needed for frontend-backend communication
from agents.data_analysis_agent import DataAnalysisAgent
from agents.location_agent import LocationAgent
from agents.rescue_agent import RescueAgent
from agents.supply_agent import SupplyAgent
from agents.communication_agent import CommunicationAgent

app = Flask(__name__)
CORS(app)  # ✅ Enables CORS for API access from your HTML page

@app.route('/')
def home():
    return "✅ Flask App Running Successfully! Visit /run-agents to execute agents."

@app.route('/run-agents')
def run_agents():
    data_agent = DataAnalysisAgent("DataAnalysisAgent")
    location_agent = LocationAgent("LocationAgent")
    rescue_agent = RescueAgent("RescueAgent")
    supply_agent = SupplyAgent("SupplyAgent")
    comm_agent = CommunicationAgent("CommunicationAgent")

    risk_message = data_agent.run()
    location_message = location_agent.run(risk_message)
    rescue_message = rescue_agent.run(location_message)
    supply_message = supply_agent.run(rescue_message)
    comm_agent.run(supply_message)

    return jsonify({
        "data_analysis": risk_message,
        "location": location_message,
        "rescue": rescue_message,
        "supply": supply_message
    })

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
