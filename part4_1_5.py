
# example part 4-20

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10,5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()

# example part 4-21

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

cylinders_size = df.cylinders/df.cylinders.max() * 300

df.plot(kind='scatter', x='weight', y='mpg', c='coral', figsize=(10,5), s=cylinders_size, alpha=0.3)
plt.title('Scatter Plot : mpg-weight-cylinders')
plt.show()

# example part 4-22

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

cylinders_size = df.cylinders/df.cylinders.max() * 300

df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10,5), cmap='viridis', c=cylinders_size, s=50, alpha=0.3)

plt.title('Scatter Plot: mpg-weight-cylinders')
plt.savefig('./scatter.png')
plt.savefig('./scatter_transparent.png', transparent=True)
plt.show()
