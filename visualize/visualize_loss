import matplotlib.pyplot as plt
import csv
import numpy as np

x=np.arange(1000)
t_loss=[None] * 1000
v_loss=[None] * 1000

with open('train_loss.csv', newline='') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:

        t_loss[int(row[0])] = (float(row[1]))

with open('validation_loss.csv', newline='') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        v_loss[int(row[0])] = (float(row[1]))

t_loss = np.array(t_loss).astype(np.double)
v_loss = np.array(v_loss).astype(np.double)

t_loss_mask = np.isfinite(t_loss)
v_loss_mask = np.isfinite(v_loss)

plt.plot(x[t_loss_mask], t_loss[t_loss_mask], marker = 'x')
plt.plot(x[v_loss_mask], v_loss[v_loss_mask], marker = 'o')
plt.show()
