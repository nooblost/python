temperatures = [19.5, 22.1, 18.0, 25.3]

print("Daily temperatures:")
for temp in temperatures:
    print(f"Temperature recorded: {temp}°C")

print("\nLoop finished.")


user_name = "Christopher"

print(f"Characters in the name {user_name}:")
for character in user_name:
    print(f"- {character}")

print("Counting from 0 to 4:")
for i in range(5):  # Generates 0, 1, 2, 3, 4
    print(i)

print("\nNumbers from 2 to 5:")
for num in range(2, 6): # Generates 2, 3, 4, 5
    print(num)

print("\nOdd numbers less than 10:")
for odd_num in range(1, 10, 2): # Generates 1, 3, 5, 7, 9
    print(odd_num)

scores = [88, 92, 75, 98, 85]
total_score = 0 # Initialize accumulator variable

for score in scores:
    total_score = total_score + score # Add current score to total

print(f"The list of scores is: {scores}")
print(f"The total score is: {total_score}")