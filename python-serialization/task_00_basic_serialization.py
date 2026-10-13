#!/usr/bin/python3
"""Basic serialization module to save and load data using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file to a Python dictionary."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
