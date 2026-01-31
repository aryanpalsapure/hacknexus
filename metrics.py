from data_constants import DATA

def calculate_metrics(plan, renewable, traffic):
    emission = DATA["traffic_emission_factor"][traffic]
    green_score = 45 if plan["green_level"] == "high" else 20

    livability = round((green_score + renewable) / emission, 2)

    return {
        "Green Coverage (%)": green_score,
        "Renewable Energy (%)": renewable,
        "Emission Level": ["Low","Medium","High"][emission-1],
        "Livability Score": livability
    }
