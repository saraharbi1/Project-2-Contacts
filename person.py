from typing import Dict

class Person:


    def __init__(self, name: str, numbers: Dict[str, int], email: str):
        self.name = name
        self.numbers = numbers
        self.email = email

    def __repr__(self):
        return f"Person(name={self.name}, numbers={self.numbers}, email={self.email})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return (
                self.name == other.name and 
                self.numbers == other.numbers and 
                self.email == other.email
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.name < other.name
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Person):
            return self.name <= other.name
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Person):
            return self.name > other.name
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Person):
            return self.name >= other.name
        return NotImplemented

    def __str__(self):
       
        numbers_str = ""
        for key, value in self.numbers.items():
            numbers_str += f"\t{key}: [{value}]\n"

        return f"{self.name}:\n{numbers_str}\temail: {self.email}"
