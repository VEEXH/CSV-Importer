import csv

# Create an empty list to store the data rows
data = []

# Print a message to the user
print("Enter your data. Press enter on an empty line to finish.")

# Loop until the user presses enter on an empty line
while True:
  # Prompt the user for a name
  name = input("Name: ")

  # If the user pressed enter on an empty line, exit the loop
  if not name:
    break

  # Prompt the user for an age
  age = input("Age: ")

  # Prompt the user for a gender
  gender = input("Gender: ")

  # Add the data as a tuple to the list
  data.append((name, age, gender))

# Open the CSV file in write mode
with open("data.csv", "w", newline="") as file:
  # Create a CSV writer object
  writer = csv.writer(file)

  # Write the column names
  writer.writerow(["Name", "Age", "Gender"])

  # Write the data rows
  writer.writerows(data)

# Print a message to the user
print("Data saved to data.csv")
