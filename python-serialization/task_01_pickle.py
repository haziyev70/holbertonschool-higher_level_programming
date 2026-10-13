#!/usr/bin/python3
"""Module for pickling and unpickling custom Python classes."""
import pickle


class CustomObject:
    """A custom class representing a person with attributes and pickle methods."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes with a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance using pickle and save to filename."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from the filename."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
