import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\problemas_graficos\\pasos.csv")
sns.lineplot(x="fecha", y="pasos", data=df)
plt.show()
