class MockAIProvider:
    async def analyse_property_viability(self, property_data, preferences, financial_analysis, image_analysis, scoring_result):
        return {"viability":"medium-high","summary":"Deterministic + mock AI analysis.","positive_signals":["Good layout"],"red_flags":["Validate building year"],"unknowns":["Building year"],"questions_to_ask":["Any pending community works?"],"negotiation_points":["Energy certificate E"],"recommended_next_steps":["Visit with technician"],"confidence":0.65}
