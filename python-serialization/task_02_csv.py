#!/usr/bin/python3
"""Module to convert CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert content of a CSV file to a JSON file (data.json)."""
    try:
        data = []
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)

        return True
    except Exception:
        return False
