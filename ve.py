from collections import Counter
counter = Counter(my_list)
for item, count in counter.items():
    if count > 1:
        print(f"{item} appears {count} times")
