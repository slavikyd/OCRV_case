import pandas as pd
db = 'hackathon_sirius_data.csv'
df = pd.read_csv(db)

def simple_allocation(df) -> list:
    tonnage_limit = df[df.columns[5]].values.tolist()
    max_train_tonnage = df[df.columns[6]].values.tolist()




    lst = []
    for i in range(0, len(tonnage_limit)):
        a = df.loc[i].values.flatten().tolist()
        lst.append([a[2], a[3]])
    output = []


    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][0] == lst[j][1] and lst[i][1] == lst[j][0]:
                print(f'pair is {lst[i]} {lst[j]}')
                temp = min(tonnage_limit[i] / max_train_tonnage[i], tonnage_limit[j] / max_train_tonnage[j])
                output.append(int(temp))
    return output

print(simple_allocation(df))