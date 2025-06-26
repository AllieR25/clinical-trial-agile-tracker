import csv

def summarize_sprint_points(csv_file):
    sprint_points = {}

    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sprint = row['Sprint']
            points = int(row['Points'])
            sprint_points[sprint] = sprint_points.get(sprint, 0) + points

    for sprint, total_points in sprint_points.items():
        print(f"{sprint}: {total_points} story points")

if __name__ == "__main__":
    summarize_sprint_points('data/sample-sprint-data.csv')
