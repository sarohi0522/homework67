# 1. Create list and find length
marks = [85, 92, 78, 90, 88]
print(f"Marks: {marks}\nStudents: {len(marks)}")

# 2. Indexing and Slicing
print(f"First: {marks[0]} | Last: {marks[-1]}")
print(f"Top 3: {marks[0:3]} | Reversed: {marks[::-1]}")

# 3. Loop and Summary Calculations
total = 0
for mark in marks:
    total += mark

print("\n--- Summary ---")
print(f"Total: {total}")
print(f"Average: {total / len(marks):.2f}")
print(f"Smallest: {min(marks)} | Largest: {max(marks)}")
