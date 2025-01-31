import matplotlib.pyplot as plt

subject  = ["Python","AI","Data Analytics","Java"]
marks = [90,85,99,80]

colors = ["Gold", "Lightblue", "Lightcoral", "Limegreen"]
explode = [0, 0, 0.1 ,0]

plt.pie(marks, labels = subject, startangle = 90, autopct = '%1.1f%%', colors = colors, explode = explode, shadow = True)
plt.title("Marks in Subjects", fontweight = "bold", size = 15)
plt.show()