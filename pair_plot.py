import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('datasets/dataset_train.csv')
df.head()
sns.pairplot(df, vars=['Arithmancy','Astronomy','Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Transfiguration','Potions','Care of Magical Creatures','Charms','Flying'], hue='Hogwarts House', diag_kind='hist', diag_kws={'bins': 10})
plt.show()