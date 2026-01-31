from supabase_client import supabase

def save_scenario(inputs, plan, metrics):
    supabase.table("city_scenarios").insert({
        "population": inputs["population"],
        "traffic": inputs["traffic"],
        "energy": inputs["energy"],
        "renewable": inputs["renewable"],
        "green_priority": inputs["green_priority"],
        "scenario": inputs["scenario"],
        "city_plan": plan,
        "metrics": metrics
    }).execute()
