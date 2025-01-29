import matplotlib.pyplot as plt

fruits = ["apple", "banana", "orange", "mango"]
quantity = [10, 20, 15, 25]


bars = plt.bar(fruits, quantity, color = "Lightcoral", edgecolor = "Black", label = "Fruits")
plt.bar_label(bars, fmt="%d", padding = 1)
plt.legend()
plt.title("Quantity Sold by Fruits", color = "Red", fontweight = "bold", size = 15)
plt.xticks(color = "Grey", rotation = 45)
plt.yticks(color = "Grey")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.grid(axis = 'y', alpha = 0.5, linestyle = "--")
plt.show()

# quantity.sort()
# bars = plt.barh(fruits, quantity, color = "Lightcoral", edgecolor = "Black", label = "Fruits")
# plt.bar_label(bars, fmt="%d", padding = 1)
# plt.legend(frameon = True, fontsize = 8)
# plt.title("Quantity Sold by Fruits", color = "Red", fontweight = "bold")
# plt.xticks(color = "Grey", fontstyle = 'italic')
# plt.yticks(color = "Grey", fontstyle = 'oblique')
# plt.xlabel("Quantity")
# plt.ylabel("Fruits")
# plt.grid(axis= 'x', alpha = 0.5, linestyle = "--")
# plt.show()