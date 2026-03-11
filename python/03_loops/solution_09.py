items = ["apple", "banana", "orange", "apple", "mango"]

uniqe_items = set()

for item in items:
    if item in uniqe_items:
        print("Oooo ji, eh ", item," to fir aa gaya")
        break
    uniqe_items.add(item)