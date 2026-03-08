import sys
import io
from contextlib import redirect_stdout

# Define exercises
exercises = [
    {
        "id": 1,
        "title": "Hello, World!",
        "level": "Easy",
        "topic": "Print",
        "description": "Write a program that prints 'Hello, World!' to the screen.",
        "hint": "Use the print() function with your message inside quotes.",
        "starter_code": "# Write your code below\n",
        "solution": 'print("Hello, World!")',
        "test": lambda output: output.strip() == "Hello, World!",
        "test_label": 'Output equals "Hello, World!"',
    },
    {
        "id": 2,
        "title": "Your Name",
        "level": "Easy",
        "topic": "Variables",
        "description": "Store your name in a variable called `name` and print: Hello, [name]!",
        "hint": "Create a variable: name = 'YourName', then use print()",
        "starter_code": "# Store your name in a variable\nname = \n",
        "solution": 'name = "Alex"\nprint("Hello, " + name + "!")',
        "test": lambda output: output.strip().startswith("Hello,") and output.strip().endswith("!"),
        "test_label": 'Output starts with "Hello," and ends with "!"',
    },
    {
        "id": 3,
        "title": "Sum of Two Numbers",
        "level": "Medium",
        "topic": "Arithmetic",
        "description": "Create two variables: a = 15, b = 27. Print their sum.",
        "hint": "Use the + operator to add numbers together.",
        "starter_code": "# Create variables a and b\na = \nb = \n# Print the sum\n",
        "solution": "a = 15\nb = 27\nprint(a + b)",
        "test": lambda output: output.strip() == "42",
        "test_label": "Output equals 42",
    },
    {
        "id": 4,
        "title": "Even or Odd",
        "level": "Medium",
        "topic": "Conditions",
        "description": "Write a program that checks if number = 7 is even or odd. Print 'Even' or 'Odd'.",
        "hint": "Use the modulus operator %. If number % 2 == 0, it's even.",
        "starter_code": "number = 7\n# Check if even or odd\n",
        "solution": "number = 7\nif number % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
        "test": lambda output: output.strip() == "Odd",
        "test_label": 'Output equals "Odd"',
    },
    {
        "id": 5,
        "title": "Count to 5",
        "level": "Medium",
        "topic": "Loops",
        "description": "Use a for loop to print numbers from 1 to 5, each on a new line.",
        "hint": "Use range(1, 6) — range goes up to but NOT including the last number.",
        "starter_code": "# Use a for loop\n",
        "solution": "for i in range(1, 6):\n    print(i)",
        "test": lambda output: output.strip() == "1\n2\n3\n4\n5",
        "test_label": "Output: 1 2 3 4 5 (each on new line)",
    },
    {
        "id": 6,
        "title": "List of Fruits",
        "level": "Hard",
        "topic": "Lists",
        "description": "Create a list with 3 fruits. Print the second fruit in the list.",
        "hint": "Lists start at index 0. So the second item is at index 1: fruits[1]",
        "starter_code": "# Create a list of 3 fruits\nfruits = []\n# Print the second fruit\n",
        "solution": 'fruits = ["apple", "banana", "cherry"]\nprint(fruits[1])',
        "test": lambda output: output.strip() and "[" not in output,
        "test_label": "Output is a single fruit name (not a list)",
    },
]

def run_code(code):
    """Run the code and capture output."""
    try:
        # Capture stdout
        f = io.StringIO()
        with redirect_stdout(f):
            exec(code)
        output = f.getvalue()
        return True, output
    except Exception as e:
        return False, str(e)

def main():
    print("THINK PYTHON - BEGINNER EXERCISES")
    print("=" * 40)

    completed = []
    selected = 0

    while True:
        ex = exercises[selected]
        print(f"\nExercise {ex['id']}: {ex['title']}")
        print(f"Level: {ex['level']} | Topic: {ex['topic']}")
        print(f"Description: {ex['description']}")
        print(f"Hint: {ex['hint']}")

        # Show starter code
        print("\nStarter Code:")
        print(ex['starter_code'])

        # Get user code
        print("Enter your code (type 'hint' for hint, 'solution' for solution, 'next' for next exercise, 'prev' for previous, 'quit' to exit). End input with an empty line:")
        user_code = ""
        while True:
            line = input()
            if line.lower() == 'hint':
                print(f"Hint: {ex['hint']}")
                continue
            elif line.lower() == 'solution':
                print("Solution:")
                print(ex['solution'])
                continue
            elif line.lower() == 'next':
                selected = (selected + 1) % len(exercises)
                break
            elif line.lower() == 'prev':
                selected = (selected - 1) % len(exercises)
                break
            elif line.lower() == 'quit':
                return
            else:
                user_code += line + "\n"
                if line.strip() == "":  # Empty line to finish
                    break

        if user_code.strip():
            success, output = run_code(user_code)
            if success:
                print("Output:")
                print(output)
                if ex['test'](output):
                    print("✅ Test Passed! Great job!")
                    if selected not in completed:
                        completed.append(selected)
                else:
                    print(f"❌ Not quite. Check: {ex['test_label']}")
            else:
                print(f"⚠️ Error: {output}")

        print(f"Completed: {len(completed)}/{len(exercises)}")

if __name__ == "__main__":
    main()