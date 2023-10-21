import pandas as pd

df = pd.read_csv("hackathon_sirius_data_edited.csv")

quantity_limit = df[df.columns[5]].values.tolist()

tonnage_limit = df[df.columns[6]].values.tolist()
max_train_tonnage = df[df.columns[7]].values.tolist()
a = df.loc[175].values.flatten().tolist()
temp = []
for i in range(0, 176):
    a = df.loc[i].values.flatten().tolist()
    if a[2] not in temp:
        temp.append(a[2])
    else:
        df.drop(index=i, inplace=True)


start = df[df.columns[2]].values.tolist()
end = df[df.columns[3]].values.tolist()


print(df)

df.to_excel('new.xlsx')