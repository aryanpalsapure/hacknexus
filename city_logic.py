def generate_city_plan(population, traffic, green_priority):
    plan = {
        "road_density": "medium",
        "residential_density": "medium",
        "green_level": "medium",
        "industrial_level": "medium"
    }

    if population == "High":
        plan["residential_density"] = "high"

    if traffic == "High":
        plan["road_density"] = "high"

    if green_priority == "High":
        plan["green_level"] = "high"
        plan["industrial_level"] = "low"

    return plan
