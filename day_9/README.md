#  Day 9 - Conditional Statements, Input, and Dictionaries

## Topics Covered
- `if`, `elif`, `else` statements
- Nested conditionals
- User input using `input()`
- Type conversion (`int()`, `float()`)
- Working with lists dynamically
- Dictionary access and operations
- Membership testing (`in`)
- Subset checks for skills

##  What I Learned
- How to take **user input** and convert it for numeric operations
- Comparing values using **nested if statements**
- Creating **dynamic responses** based on conditions
- Accessing dictionary keys and nested structures
- Checking subsets in lists for logic decisions

##  Exercises Completed
### Level 1
- Age checking for driving
- Compare ages
- Compare two numbers

### Level 2
- Assign grades based on scores
- Determine season from month input
- Dynamic fruits list modification

### Level 3
- Accessing dictionary skills
- Middle skill extraction
- Developer role determination
- Combined conditional checks (married + location)


## Sample Highlight

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")
