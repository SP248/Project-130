import pandas

df = pandas.read_csv("")
df = df.dropna()
df = df.drop_duplicates()

del df["luminosity"]
del df["distance"]
del df["mass"]
del df["radius"]

df.rename(columns={"": "", })

df.to_csv("", index=False)