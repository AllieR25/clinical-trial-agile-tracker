"""
sprint_kpi_report.py

Generates a mock report of key Agile metrics across clinical trial sprints.
"""

# Sample data (replace with real data or integrations later)
sprint_data = [
    {"sprint": "Sprint 1", "velocity": 30, "defects": 2, "burn_down": "On Track"},
    {"sprint": "Sprint 2", "velocity": 27, "defects": 4, "burn_down": "Slight Delay"},
]

def generate_report(data):
    print("📊 Sprint KPI Report")
    print("-" * 25)
    for item in data:
        print(f"Sprint: {item['sprint']}")
        print(f"Velocity: {item['velocity']} story points")
        print(f"Defects: {item['defects']}")
        print(f"Burndown Status: {item['burn_down']}")
        print("")

if __name__ == "__main__":
    generate_report(sprint_data)
