import matplotlib.pyplot as plt
import csv

x = []
y = []
x1 = []
y1 = []

with open('logs/mlplogs.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append((row[5]))

plt.plot(x, y, color='blue', markersize=12,label="MLP")

with open('logs/svmlogs.csv','r') as csvfile:
    plot2 = csv.reader(csvfile, delimiter=',')
    for row in plot2:
        x1.append((row[0]))
        y1.append((row[5]))

plt.plot(x1, y1, color='red', markersize=12, label = "SVM")

plt.xlabel('epoch')
plt.ylabel('Accuracy')
plt.title('Epoch vs Accuracy for MLP and SVM')
plt.legend()
plt.show()