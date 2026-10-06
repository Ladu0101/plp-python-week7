# Part C — List Report
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
count = 0
for item in items:
    if len(item) > 4:
        count += 1
print(count)


longest_name = ""
for item in items:
    if len(item) > len(longest_name):
        longest_name = item
print(longest_name)