import random

# Step 1: List of names (you can expand this list)
names = [
    "Alice", "Anna", "Albert", "Amelia", "Aaron", "Bob", "Bill", "Billy", 
    "Ben", "Beverly", "Charlotte", "Chris", "Catherine", "Caleb", "David", 
    "Diana", "Daniel", "Daniela", "Edward", "Ella", "Ethan", "Eva", 
    "Fiona", "Frank", "Francis", "Felicity", "George", "Grace", "Gabriel", 
    "Hannah", "Harold", "Helen", "Henry", "Ivy", "Isaac", "Irene", 
    "Jack", "James", "Jill", "Julia", "Joseph", "Katherine", "Kevin", 
    "Karen", "Liam", "Laura", "Luke", "Lily", "Michael", "Megan", "Maggie", 
    "Nathan", "Nina", "Nicholas", "Olivia", "Oscar", "Owen", "Peter", 
    "Paul", "Patricia", "Quinn", "Rachel", "Randy", "Ruth", "Samuel", 
    "Sophia", "Steve", "Susan", "Thomas", "Tina", "Tim", "Victoria", 
    "Vera", "William", "Wendy", "Walter", "Xander", "Xena", "Yvonne", "Zoe", "Vivek", "Viksha" , "Varanasi", "Lakshmi", "Vivansh"
]

# Step 2: Function to generate random names based on first letter
def generate_name(first_letter, num_names=5):
    # Filter names based on the first letter
    filtered_names = [name for name in names if name.lower().startswith(first_letter.lower())]
    
    if not filtered_names:
        return f"No names found starting with {first_letter.upper()}"
    
    # Generate random names from the filtered list
    random_names = random.sample(filtered_names, min(num_names, len(filtered_names)))
    
    return random_names

# Step 3: Example Usage
first_letter = input("Enter the first letter of the name you want to generate: ").strip()
num_names = int(input("How many names do you want to generate? "))

# Generate and print random names
generated_names = generate_name(first_letter, num_names)

print(f"Generated names starting with '{first_letter.upper()}':")
for name in generated_names:
    print(name)
