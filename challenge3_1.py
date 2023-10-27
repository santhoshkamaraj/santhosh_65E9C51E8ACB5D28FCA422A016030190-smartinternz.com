def linear_search_product(product_list, target_product):
  indices = []

  for i in range(len(product_list)):
      if product_list[i] == target_product:
          indices.append(i)

  return indices

n = int(input("ENTER THE NUMBER OF ITEMS IN PRODUCT LIST:"))
strings = []
print(f"ENTER THE {n} ITEMS")
for j in range(n):
  product = input()
  strings.append(product)

target = input("ENTER THE TARGET PRODUCT TO SEARCH: ")
result = linear_search_product(strings, target)

if result:
  print(f"Indices of target product '{target}': {result}")
else:
  print(f"Target product '{target}' not found in the list.")