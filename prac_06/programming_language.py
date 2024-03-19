"""
Start Time : 1:30pm
  End Time : 2:11pm
Total Time : 41 minutes

Experience: Either my brain is not working today or the practical is written poorly.
It took me a while to understand what the practical is telling me to do
"""


class ProgrammingLanguage:
    def __init__(self, language_name, typing, reflection, year):
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.language_name}, {self.typing} Typing, Reflection={self.reflection}, {self.year}"
