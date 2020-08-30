
import pandas as pd

""" purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 1', 'Store 2'])
print(df.head())
 """

""" df = pd.read_csv('olympics.csv')

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

print(df['Gold'])
 """
""" purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 1', 'Store 2'])


df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(
    data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
print(df) """


df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        df.rename(columns={col: '#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(')  # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
# the [1] element is the abbreviation or ID (take first 3 characters from that)
df['ID'] = names_ids.str[1].str[:3]

df = df.drop('Totals')
#print(df.head())

#print(df.sort_values(by=['Gold'], ascending=False).iloc[0][0])
#print(df.iloc[:146, 2].idxmax())
#tempdf = df((df.iloc[0:146, 2] - df.iloc[0:146, 6]))

#print(tempdf.iloc[:146, 2].idxmax())
#df['points'] = 3 * (df['Gold'].sum(axis=1)) + 2 * (df['Silver'].sum(axis=1)) + 1 * (df['Bronze'].sum(axis=1))
#print(df.iloc[:, 14])
print(df['Gold'].idxmax())
