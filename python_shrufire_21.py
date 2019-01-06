import pandas as pd
rate=pd.read_csv("Dec21-Exchange_Rates.csv")
rate2= rate.set_index("LOCATION", drop = False)
src=input('From Country: ')
org_mon=int(input('Money I have: '))
des=input('To Country: ')
sf=rate2.loc[src]
df=rate2.loc[des]
src_cur=float(sf.loc['VALUE'])
des_cur=float(df.loc['VALUE'])
fin_mon=(org_mon*src_cur)/des_cur
print(org_mon,' (',src,') = ',fin_mon,' (',des,')')


