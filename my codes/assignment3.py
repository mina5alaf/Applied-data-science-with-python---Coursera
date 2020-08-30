import pandas as pd
import numpy as np

def answer_one():
    energy = pd.read_excel('Energy Indicators.xls', skiprows=17, skip_footer=38)
    energy = energy[['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']]
    energy.columns = ['Country', 'Energy Supply',
                    'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] = energy[[
        'Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...', np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region': 'Hong Kong', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                                'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'Iran (Islamic Republic of)': 'Iran'})
    energy['Country'] = energy['Country'].str.replace(" \(.*\)", "")

    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Korea, Rep.', 'South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Iran, Islamic Rep.', 'Iran')
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Hong Kong SAR, China', 'Hong Kong')

    columns = ['Country Name', '2006', '2007', '2008',
            '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    GDP = GDP[columns]

    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    ScimEn_m = ScimEn[:15]

    df = pd.merge(ScimEn_m, energy, how='inner',
                left_on='Country', right_on='Country')
    final_df = pd.merge(df, GDP, how='inner',
                        left_on='Country', right_on='Country Name')
    final_df = final_df.set_index('Country')
    columns = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply',
            'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    ans = final_df[columns]
    return ans


answer_one()
 
 #------------------------------------------------------------------------------------

def answer_two():
    energy = pd.read_excel('Energy Indicators.xls',
                           skiprows=17, skip_footer=38)
    energy = energy[['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']]
    energy.columns = ['Country', 'Energy Supply',
                      'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] = energy[[
        'Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...', np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region': 'Hong Kong', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                                   'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'Iran (Islamic Republic of)': 'Iran'})
    energy['Country'] = energy['Country'].str.replace(" \(.*\)", "")

    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Korea, Rep.', 'South Korea')
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Iran, Islamic Rep.', 'Iran')
    GDP['Country Name'] = GDP['Country Name'].replace(
        'Hong Kong SAR, China', 'Hong Kong')

    columns = ['Country Name', '2006', '2007', '2008', '2009',
               '2010', '2011', '2012', '2013', '2014', '2015']

    GDP = GDP[columns]
    GDP.columns = ['Country', '2006', '2007', '2008', '2009',
                   '2010', '2011', '2012', '2013', '2014', '2015']

    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    ScimEn_m = ScimEn[:15]

    df = pd.merge(ScimEn, energy, how='inner',
                  left_on='Country', right_on='Country')
    final_df = pd.merge(df, GDP, how='inner',
                        left_on='Country', right_on='Country')
    final_df = final_df.set_index('Country')
    columns = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply',
               'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    ans = final_df[columns]

    df2 = pd.merge(ScimEn, energy, how='outer',
                   left_on='Country', right_on='Country')
    final_df2 = pd.merge(df2, GDP, how='outer',
                         left_on='Country', right_on='Country')

    print(len(final_df))
    print(len(final_df2) - len(final_df))


answer_two()

#-----------------------------------------------------------------------


def answer_three():
    import numpy as np
    Top15 = answer_one()
    columns = ['2006', '2007', '2008', '2009', '2010',
               '2011', '2012', '2013', '2014', '2015']
    Top15['Mean'] = Top15[columns].mean(axis=1)
    avgGDP = Top15.sort_values(by='Mean', ascending=False)['Mean']
    return avgGDP


answer_three()

#-----------------------------------------------------


def answer_four():
    Top15 = answer_one()
    columns = ['2006', '2007', '2008', '2009', '2010',
               '2011', '2012', '2013', '2014', '2015']
    Top15['Mean'] = Top15[columns].mean(axis=1)
    avgGDP = Top15.sort_values(by='Mean', ascending=False)['Mean']
    target = avgGDP.index[5]
    target_data = Top15.loc[target]
    ans = target_data['2015'] - target_data['2006']
    return ans


answer_four()

#------------------------------------------------------


def answer_five():
    Top15 = answer_one()
    target = Top15['Energy Supply per Capita']
    ans = target.mean()
    return ans


answer_five()


#-------------------------------------------------------


def answer_six():
    Top15 = answer_one()
    target = Top15['% Renewable']
    ans = target.max()
    index = Top15[Top15['% Renewable'] == ans].index[0]
    return (index, ans)


answer_six()


#--------------------------------------------------------


def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations'] / Top15['Citations']
    target = Top15['Ratio']
    max_value = target.max()
    max_index = Top15[Top15['Ratio'] == max_value].index[0]
    return (max_index, max_value)


answer_seven()


#---------------------------------------------------------------


def answer_eight():
    Top15 = answer_one()
    columns = ['Energy Supply', 'Energy Supply per Capita']
    target = Top15[columns]
    target['Captita'] = Top15['Energy Supply'] / \
        Top15['Energy Supply per Capita']
    ans = target.sort_values(by='Captita', ascending=False).iloc[2].name
    return ans


answer_eight()


#---------------------------------------------------------------


def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / \
        Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    ans = Top15['Citable docs per Capita'].corr(
        Top15['Energy Supply per Capita'])
    return ans


answer_nine()


#---------------------------------------------------------


def answer_ten():
    import pandas as pd
    Top15 = answer_one()
    med = Top15['% Renewable'].median()
    Top15['HighRenew'] = [1 if x >= med else 0 for x in Top15['% Renewable']]
    ans = Top15['HighRenew']
    return pd.Series(ans)


answer_ten()


#----------------------------------------------------------


def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] /
                       Top15['Energy Supply per Capita'])
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country]
                          for country in Top15['Country']]
    target = Top15.set_index('Continent').groupby(level=0)['PopEst'].agg(
        {'size': np.size, 'sum': np.sum, 'mean': np.mean, 'std': np.std})
    ans = target[['size', 'sum', 'mean', 'std']]
    return ans


answer_eleven()


#-----------------------------------------------------------------


def answer_twelve():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    Top15 = answer_one()
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country]
                          for country in Top15['Country']]
    Top15['bins'] = pd.cut(Top15['% Renewable'], 5)

    ans = Top15.groupby(['Continent', 'bins']).size()
    return pd.Series(ans)


answer_twelve()


#----------------------------------------------------------



