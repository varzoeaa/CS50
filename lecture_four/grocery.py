items = {}
while True:
    item = input("Enter item (or 'STOP' to finish): ")
    if item.strip().lower() == 'stop':
        break
    normalized_item = item.strip().lower()  
    if normalized_item in items:
        items[normalized_item] += 1
    else:
        items[normalized_item] = 1

print("\nGrocery list:")
for item, count in sorted(items.items()):  # alphabetical order
    print(f"{count} {item.upper()}")  # uppercase

'''
stop because ctrl + c doesnt work with vscode
'''