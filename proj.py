import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("1.csv", delimiter=',')
print('1- Россия, 2-Украина, 3-Белорусь')
count = int(input())
#year = int(input())
#year1 = 'Y'+str(year)
data_RUS = data[data['Country Code'] == 'RUS']
data_UKR = data[data['Country Code'] == 'UKR']
data_BLR = data[data['Country Code'] == 'BLR']
print(data_BLR,data_RUS,data_UKR)
#df_RUS = data_RUS.loc[:, year1]
#df_UKR = data_UKR.loc[:, year1]
#df_BLR = data_BLR.loc[:, year1]
df_RUS = data_RUS.iloc[:, 4+1995-1995:5+2019-1995]
df_UKR = data_UKR.iloc[:, 4+1995-1995:5+2019-1995]
df_BLR = data_BLR.iloc[:, 4+1995-1995:5+2019-1995]
if count == 1:
    np_df = np.array(df_RUS)
elif count == 2:
    np_df = np.array(df_UKR)
else:
    np_df = np.array(df_BLR)
print(np_df[0])

d = {'Сельхоз.перепись': np_df[1], 'Рук.по плат. бал. в исп.': np_df[2], 'Детск.недоед.': np_df[3],
     'Инд.потр.цен': np_df[5], 'Стат.отч.по вн.долг': np_df[6], 'Генд.рав.': np_df[7], 'Гос.фин.учет': np_df[8],
     'Здравохр.': np_df[9], 'ВИЧ': np_df[10], 'Имун': np_df[11], 'Бедн.': np_df[13],
     'Инд.пром.произ.': np_df[14], 'оцен.стат.пот.': np_df[16], 'нац.счет': np_df[17],
     'общ.сред.пок.': np_df[19], 'ВВП': np_df[20],
     'Период. и своеврем.оц.стат.пот.': np_df[21], 'Переп.нас.': np_df[22], 'Нач.обр': np_df[24], 'Исх.дан.оц.статист.пот.': np_df[25],
     'Спец.стан.распрост.дан.': np_df[26], 'Отч.ЮНЕСКО': np_df[27], 'Охв.жиз.важ.сист.рег.': np_df[28]}

cor = pd.DataFrame(data=d,
                   columns=['Сельхоз.перепись', 'Рук.по плат. бал. в исп.', 'Детск.недоед.', 'Инд.потр.цен', 'Стат.отч.по вн.долг', 'Генд.рав.', 'Гос.фин.учет',
                            'Здравохр.', 'ВИЧ', 'Имун', 'Бедн.', 'Инд.пром.произ.', 'оцен.стат.пот.', 'нац.счет',
                            'общ.сред.пок.', 'ВВП',
                            'Период. и своеврем.оц.стат.пот.', 'Переп.нас.', 'Нач.обр', 'Исх.дан.оц.статист.пот.', 'Спец.стан.распрост.дан.', 'Отч.ЮНЕСКО', 'Охв.жиз.важ.сист.рег.'])
plt.figure(figsize=(29, 29), dpi=58)
sns.heatmap(cor.corr(), xticklabels=cor.corr().columns, yticklabels=cor.corr().columns, cmap='RdYlGn', center=0, vmin= -1, vmax= 1,
            annot=True)




plt.title('Матрица корреляции', fontsize=80)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
