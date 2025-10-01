import pandas as pd
import numpy as np

# 1986 - 2010

dd = pd.read_csv('orig/lotto-ergebnisse-1986-2010.csv.gz', encoding='latin-1', sep=';')
dd.columns = [f'c{i}' for i in range(dd.shape[1])]
dd = dd.dropna(how='all', axis=1).dropna(how='all', axis=0)
dd = dd.loc[~dd['c4'].isna()]
dd = dd.drop(columns=['c0', 'c8', 'c11', 'c14', 'c17', 'c20', 'c23', 'c25', 'c26', 'c27', 'c28', 'c29', 'c30', 'c31', 'c32'])
dd = dd.rename(columns={
    'c1': 'Datum',
    'c2': 'Zahl 1',
    'c3': 'Zahl 2',
    'c4': 'Zahl 3',
    'c5': 'Zahl 4',
    'c6': 'Zahl 5',
    'c7': 'Zahl 6',
    'c9': 'Zusatzzahl',
    'c10': '6er - Gewinne',
    'c12': '6er - Betrag',
    'c13': '5er + ZZ - Gewinne',
    'c15': '5er + ZZ - Betrag',
    'c16': '5er - Gewinne',
    'c18': '5er - Betrag',
    'c19': '4er - Gewinne',
    'c21': '4er - Betrag',
    'c22': '3er - Gewinne',
    'c24': '3er - Betrag',
})
for c in [f'Zahl {i}' for i in [1,2,3,4,5,6]] + ['Zusatzzahl']:
    dd[c] = dd[c].astype(int)
for c in dd.columns:
    if c.endswith('Betrag'):
        dd[c] = dd[c].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    if c.endswith('Gewinne'):
        dd[c] = dd[c].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
dd.at[2214, "6er - Betrag"] = "808317.30" # fix data entry
dd = dd.reset_index(drop=True)
dd['Datum'] = pd.to_datetime(dd['Datum'].str.replace(' ', '') + '1988', format="%d.%m.%Y")
year = 1986
for i in range(len(dd)):
    dd.at[i, 'Datum'] = dd.at[i, 'Datum'].replace(year=year)
    if i < len(dd) - 1 and dd['Datum'].dt.month[i+1] == 1 and dd['Datum'].dt.month[i] == 12:
        year += 1
d1 = dd.copy()


# 2010 - 2017

df = pd.read_csv('orig/lotto-ziehungen-2010-2017.csv.gz', encoding='latin-1', sep=';')
df.columns = [f'c{i}' for i in range(df.shape[1])]
df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)
df = df.loc[~df['c4'].isna()]
df = df.drop(columns=['c0', 'c2', 'c9', 'c13', 'c17', 'c21', 'c25'])
df1 = df.iloc[[(2*i) for i in range(len(df)//2)]].reset_index(drop=True)
df2 = df.iloc[[(2*i)+1 for i in range(len(df)//2)]].reset_index(drop=True).add_prefix('x')
dd = pd.concat([df1, df2], axis=1).reset_index(drop=True)
dd = dd.drop(columns=['xc1'])
dd = dd.rename(columns={
    'c1': 'Datum',
    'c3': 'Zahl 1',
    'c4': 'Zahl 2',
    'c5': 'Zahl 3',
    'c6': 'Zahl 4',
    'c7': 'Zahl 5',
    'c8': 'Zahl 6',
    'c10': 'Zusatzzahl',
    'c12': '6er - Gewinne',
    'c14': '6er - Betrag',
    'c16': '5er + ZZ - Gewinne',
    'c18': '5er + ZZ - Betrag',
    'c20': '5er - Gewinne',
    'c22': '5er - Betrag',
    'c24': '4er + ZZ - Gewinne',
    'c26': '4er + ZZ - Betrag',
    'xc12': '4er - Gewinne',
    'xc14': '4er - Betrag',
    'xc16': '3er + ZZ - Gewinne',
    'xc18': '3er + ZZ - Betrag',
    'xc20': '3er - Gewinne',
    'xc22': '3er - Betrag',
    'xc24': 'ZZ - Gewinne',
    'xc26': 'ZZ - Betrag',
}).drop(columns=['c11', 'c15', 'c19', 'c23', 'xc11', 'xc15', 'xc19', 'xc23', 'xc3', 'xc4', 'xc5', 'xc6', 'xc7', 'xc8', 'xc10', 'xc11'])
for c in [f'Zahl {i}' for i in [1,2,3,4,5,6]] + ['Zusatzzahl']:
    dd[c] = dd[c].astype(int)
for c in dd.columns:
    if c.endswith('Betrag'):
        dd[c] = dd[c].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    if c.endswith('Gewinne'):
        dd[c] = dd[c].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
dd['Datum'] = pd.to_datetime(dd['Datum'].str.replace(' ', '') + '1988', format="%d.%m.%Y")
year = 2010
for i in range(len(dd)):
    dd.at[i, 'Datum'] = dd.at[i, 'Datum'].replace(year=year)
    if i < len(dd) - 1 and dd['Datum'].dt.month[i+1] == 1 and dd['Datum'].dt.month[i] == 12:
        year += 1
d2 = dd.copy()


# 2018 - 2025

dfs = []
for y in [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]:
    print(y)
    fn = f'orig/NN_W2D_STAT_Lotto_{y}.csv.gz'
    df = pd.read_csv(fn, encoding='latin-1', sep=';', dtype='str')
    df1 = df.iloc[[(2*i) for i in range(len(df)//2)]].reset_index(drop=True)
    df2 = df.iloc[[(2*i)+1 for i in range(len(df)//2)]].reset_index(drop=True).add_prefix('x')
    dd = pd.concat([df1, df2.drop(columns=['xDatum'])], axis=1)
    dd['Datum'] = dd['Datum'] + str(y)
    dd = dd.drop(columns=['Reihenfolge', 'ZZ', 'Rang_1_5', 'Rang_2_6', 'Rang_3_7', 'Rang_4_8', 'a_1_5', 'a_2_6', 'a_3_7', 'a_4_8', 'Unnamed: 26'])
    dd = dd.drop(columns=['xReihenfolge', 'xZZ', 'xRang_1_5', 'xRang_2_6', 'xRang_3_7', 'xRang_4_8', 'xa_1_5', 'xa_2_6', 'xa_3_7', 'xa_4_8', 'xUnnamed: 26'])
    dd = dd.drop(columns=[f'xZahl{i}' for i in [1,2,3,4,5,6]] + ['xZusatzzahl'])
    dd = dd.rename(columns={'Zahl1': 'Zahl 1', 'Zahl2': 'Zahl 2', 'Zahl3': 'Zahl 3', 'Zahl4': 'Zahl 4', 'Zahl5': 'Zahl 5', 'Zahl6': 'Zahl 6'})
    dd = dd.rename(columns={'Anzahl_1_5': '6er - Gewinne', 'Quote_1_5': '6er - Betrag'})
    dd = dd.rename(columns={'Anzahl_2_6': '5er ZZ - Gewinne', 'Quote_2_6': '5er ZZ - Betrag'})
    dd = dd.rename(columns={'Anzahl_3_7': '5er - Gewinne', 'Quote_3_7': '5er - Betrag'})
    dd = dd.rename(columns={'Anzahl_4_8': '4er ZZ - Gewinne', 'Quote_4_8': '4er ZZ - Betrag'})
    dd = dd.rename(columns={'xAnzahl_1_5': '4er - Gewinne', 'xQuote_1_5': '4er - Betrag'})
    dd = dd.rename(columns={'xAnzahl_2_6': '3er ZZ - Gewinne', 'xQuote_2_6': '3er ZZ - Betrag'})
    dd = dd.rename(columns={'xAnzahl_3_7': '3er - Gewinne', 'xQuote_3_7': '3er - Betrag'})
    dd = dd.rename(columns={'xAnzahl_4_8': 'ZZ - Gewinne', 'xQuote_4_8': 'ZZ - Betrag'})
    for c in [f'Zahl {i}' for i in [1,2,3,4,5,6]] + ['Zusatzzahl']:
        dd[c] = dd[c].astype(int)
    for c in dd.columns:
        if c.endswith('Betrag'):
            dd[c] = dd[c].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        elif c == '5er - Gewinne':
            dd[c] = dd[c].astype("Int64")
        elif c.endswith('Gewinne'):
            dd[c] = dd[c].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    dd['Datum'] = pd.to_datetime(dd['Datum'], format="%d.%m.%Y")
    dfs.append(dd)
df = pd.concat(dfs).reset_index(drop=True)
d3 = df.copy()


# CONCAT

df = pd.concat([d1, d2, d3],axis=0)[d3.columns]
df['6er - Betrag'] = df['6er - Betrag'].astype(str).str.replace('1 ', '').astype(float)
df['Datum'] = pd.to_datetime(df['Datum'])
idx = df.Datum.dt.year < 2001
for col in df:
    if col.endswith('Betrag'):
        df[col] = df[col].where(-idx, (df[col].astype(float) / 13.7602).round(2))
        df[col] = df[col].astype("Float64")
    if col.endswith('Gewinne') and df.dtypes[col] != 'object':
        df[col] = df[col].astype("Int64")
df['6er - Gewinne'] = df['6er - Gewinne'].str.strip().replace({'2JP': 'DJP', '2 JP': 'DJP', '3 JP': '3JP', '3-JP': '3JP', '0': 'JP'})
df['5er ZZ - Gewinne'] = df['5er ZZ - Gewinne'].str.strip().replace({'2JP': 'DJP', '2 JP': 'DJP', '3 JP': '3JP', '3-JP': '3JP', '0': 'JP'})
df['4er ZZ - Gewinne'] = df['4er ZZ - Gewinne'].astype("Int64")
df['4er - Gewinne'] = df['4er - Gewinne'].astype("Int64")
df['3er ZZ - Gewinne'] = df['3er ZZ - Gewinne'].astype("Int64")
df['3er - Gewinne'] = df['3er - Gewinne'].astype("Int64")
df['ZZ - Gewinne'] = df['ZZ - Gewinne'].astype("Int64")

df['6er - Ausbezahlt'] = df['6er - Gewinne'].fillna("0").mask(df['6er - Gewinne'].fillna("0").str.endswith('JP'), 0).astype(int) * df['6er - Betrag']
df['5er ZZ - Ausbezahlt'] = df['5er ZZ - Gewinne'].fillna("0").mask(df['5er ZZ - Gewinne'].fillna("0").str.endswith('JP'), "0").astype(int) * df['5er ZZ - Betrag']
df['5er - Ausbezahlt'] = df['5er - Gewinne'].astype(float) * df['5er - Betrag'].astype(float)
df['4er ZZ - Ausbezahlt'] = df['4er ZZ - Gewinne'].astype(float) * df['4er ZZ - Betrag'].astype(float)
df['4er - Ausbezahlt'] = df['4er - Gewinne'].astype(float) * df['4er - Betrag'].astype(float)
df['3er ZZ - Ausbezahlt'] = df['3er ZZ - Gewinne'].astype(float) * df['3er ZZ - Betrag'].astype(float)
df['3er - Ausbezahlt'] = df['3er - Gewinne'].astype(float) * df['3er - Betrag'].astype(float)
df['ZZ - Ausbezahlt'] = df['ZZ - Gewinne'].astype(float) * df['ZZ - Betrag'].astype(float)
df['Gesamt - Ausbezahlt'] = (
    df['6er - Ausbezahlt'].fillna(0).astype(float) + 
    df['5er ZZ - Ausbezahlt'].fillna(0).astype(float) +
    df['5er - Ausbezahlt'].fillna(0).astype(float) +
    df['4er ZZ - Ausbezahlt'].fillna(0).astype(float) +
    df['4er - Ausbezahlt'].fillna(0).astype(float) +
    df['3er ZZ - Ausbezahlt'].fillna(0).astype(float) +
    df['3er - Ausbezahlt'].fillna(0).astype(float) +
    df['ZZ - Ausbezahlt'].fillna(0).astype(float)
)

df['Datum'] = pd.to_datetime(df['Datum']).dt.date
df = df.reset_index(drop=True)
df = df[['Datum',
 'Zahl 1',
 'Zahl 2',
 'Zahl 3',
 'Zahl 4',
 'Zahl 5',
 'Zahl 6',
 'Zusatzzahl',
 'Gesamt - Ausbezahlt',
 '6er - Gewinne',
 '6er - Betrag',
 '6er - Ausbezahlt',
 '5er ZZ - Gewinne',
 '5er ZZ - Betrag',
 '5er ZZ - Ausbezahlt',
 '5er - Gewinne',
 '5er - Betrag',
 '5er - Ausbezahlt',
 '4er ZZ - Gewinne',
 '4er ZZ - Betrag',
 '4er ZZ - Ausbezahlt',
 '4er - Gewinne',
 '4er - Betrag',
 '4er - Ausbezahlt',
 '3er ZZ - Gewinne',
 '3er ZZ - Betrag',
 '3er ZZ - Ausbezahlt',
 '3er - Gewinne',
 '3er - Betrag',
 '3er - Ausbezahlt',
 'ZZ - Gewinne',
 'ZZ - Betrag',
 'ZZ - Ausbezahlt',
]]
df['6er - Pott Start'] = df['6er - Betrag'].shift(1).where(df['6er - Gewinne'].shift(1).str.endswith('JP'))
df['6er - Pott Bonus'] = (df['6er - Betrag'] - df['6er - Pott Start'].fillna(0)).round(2)
for col in df.select_dtypes(float):
  df[col] = df[col].round(2)
df = df.sort_values('Datum', ascending=False)

# sort zahlen
cols = ['Zahl 1', 'Zahl 2', 'Zahl 3', 'Zahl 4', 'Zahl 5', 'Zahl 6']
df[cols] = np.sort(df[cols].values, axis=1)

df.columns = [c.replace('Gewinne', 'Gewinner') for c in df.columns]

df.to_csv('lotto-1986-2025.csv', index=False)
