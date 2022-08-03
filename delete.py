import csv
import pandas as pd


df = pd.read_csv("dwarf_stars.csv")

df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

df = df.drop(labels ='Unnamed: 0', axis = 1)

df.to_csv("dwarf_updated.csv")




