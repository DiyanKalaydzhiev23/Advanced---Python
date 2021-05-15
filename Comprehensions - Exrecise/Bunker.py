categories = {category: [] for category in input().split(", ")}
total_quantity = 0
total_quality = 0

for _ in range(int(input())):
    category, item, quantity_quality = input().split(" - ")
    categories[category].append(item)
    quantity, quality = [info.split(":")[1] for info in quantity_quality.split(";")]
    total_quantity += int(quantity)
    total_quality += int(quality)

print(f"Count of items: {total_quantity}")
print(f"Average quality: {total_quality/len(categories):.2f}")
[print(f"{category} -> {', '.join(categories[category])}") for category in categories]
