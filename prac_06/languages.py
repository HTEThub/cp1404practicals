"""
Start Time : 1:30pm
  End Time : 2:11pm
Total Time : 41 minutes

Experience: Either my brain is not working today or the practical is written poorly.
It took me a while to understand what the practical is telling me to do
"""


from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]
print("The dynamically typed languages are: ")
for eachLanguage in languages:
    if eachLanguage.is_dynamic():
        print(eachLanguage.language_name)
