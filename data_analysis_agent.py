from google.cloud import bigquery
from adk.agent import Agent

class DataAnalysisAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.client = bigquery.Client()

    def run(self):
        query = """
        SELECT region, flood_risk_score
        FROM `dynamic-music-428408-t7.t7.flood_risk_scores_full`
        ORDER BY flood_risk_score DESC
        LIMIT 5
        """
        result = self.client.query(query)
        top_regions = [row['region'] for row in result]
        print(f"[DataAnalysisAgent] High Risk Regions: {top_regions}")
        self.send("LocationAgent", {"risk_zones": top_regions})
        return {"risk_zones": top_regions}
