entry = input("Write your journal entry: ")

with open("journal.txt", "a") as file:
    file.write(entry + "\n")

print("✅ Entry saved!")
