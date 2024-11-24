import json
import csv

with open('/Users/xzl/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
with open('chacon.csv', 'w') as csv_file:

    for repo in data[:5]:
        name = repo.get('name')
        html_url = repo.get('html_url')
        updated_at = repo.get('updated_at')
        visibility = repo.get('visibility')
        csv_line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(csv_line)

print("CSV file chacon.csv has been created with the first 5 repositories.")


