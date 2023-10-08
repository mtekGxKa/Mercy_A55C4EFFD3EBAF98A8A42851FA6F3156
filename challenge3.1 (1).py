#3.1  Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.

def linearSearchProduct(ProductList, targetProduct):
  indicates=[]

  for index,Product in enumerate(ProductList):
    if Product == targetProduct:
      indicates.append(index)
  return indicates


Products=["shoes", "boot","loafer","shoes","sandal","shoes"]
target="shoes"
target2="apple"
result=linearSearchProduct(Products, target)
print(result)