import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")

print()
print("Using the .shape command provides the information:")
print(titanic.shape)
print()
print("Using the .columns command provides the information:")
print(titanic.columns)
print()
print("Using the .dtypes command provides the information:")
print(titanic.dtypes)
print()
