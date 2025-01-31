import matplotlib.pyplot as plt

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
sales = [160, 150, 170, 175, 160, 190, 180]

plt.plot(days, sales, label = "Sales", color = "Orange", marker = "s", linewidth = 2, linestyle = "--")

for i in range(len(days)):
    plt.text(days[i], sales[i], f'{sales[i]}', ha='center', va='bottom', fontsize=10)

plt.title("Sales over Days", fontweight = "bold", size = 17)
plt.legend(frameon = True, fontsize = 8, loc = "upper left")
plt.xticks(color = "Black", rotation = 45)
plt.yticks(color = "Black")
plt.xlabel("Days", color = "Grey")
plt.ylabel("Sales", color = "Grey")
plt.grid(axis = "both", alpha = 0.4)
plt.show()