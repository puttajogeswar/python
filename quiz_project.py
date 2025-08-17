question_bank=[
    {"text":"1. Which of the following defines a class in Python? ","answer":"B"},
    {"text":"2. Which method is called automatically when an object is created? ","answer":"C"},
    {"text":"3. Which of the following is NOT a type of inheritance in Python?","answer":"D"},
    {"text":"4. What is method overriding in Python?","answer":"B"},
    {"text":"5. What is the correct syntax to access a class variable inside a method?","answer":"A"}
    ]

options=[
   ["A. def MyClass",
    "B. class MyClass", 
    "C. create MyClass",
    "D. object MyClass",],
    ["A. __new__()",
    "B. __str__()",
    "C. __init__()",
    "D. __start__()"],
   ["A. Single inheritance",
    "B. Multiple inheritance",
    "C. Multilevel inheritance",
    "D. Functional inheritance "],
   ["A. Writing multiple methods with the same name in the same class",
    "B. Writing a method in a subclass with the same name as in its superclass",
    "C. Writing two methods with different names in the same class",
    "D. Rewriting a function from Python’s built-in library"],
    ["A. self.variable_name",
    "B. cls.variable_name",
    "C. this.variable_name",
    "D. variable_name"]
   ]

def check_answer(n,check):
    if n==check:
        return True
    else:
        return False
    
score=0
for i in range(len(question_bank)):
    print(question_bank[i]["text"])
    for j in range(4):
        print(options[i][j])
    n=input("Enter a option ").upper()
    ans=check_answer(n,question_bank[i]["answer"])
    if ans==True:
        score+=1
        print(f"you are correct Score is {score}/5")
    else:
        print("Incorrect answer ")
        print("Correct answer is ",question_bank[i]["answer"])
    print()
    print()
print(f" your final score is {score/5*100} ")







