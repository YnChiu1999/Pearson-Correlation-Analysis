import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Periodic_Element_Table_heatmap import polt_elemTable
import seaborn as sns

df = pd.read_excel("data.xlsx" , sheet_name="Eta'_PIS_all", usecols="A:V", header=27)

# ## grep Element ===============================================================================
ele_isnalist = df['Element'].isna().tolist()
for i in ele_isnalist:
    if i == True:
        # df = df.drop([ii])
        df.drop(df.tail(ele_isnalist.index(i)).index,inplace=True)
        break
    elif i == False: pass # print(i, j)
    else: print("Error")

# ## remove rows with NAN value  ===============================================================
col = []
col.append('Metallic Radius (pm)')       # col[0]
col.append('Pauling electronegativity')    # col[1]
col.append('Electron affinity (eV)')     # col[2]
col.append('Segregation energy (eV/lattice)')             # col[3]

# 去除干擾元素 ===========================================================================
# df = df.drop(index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 20, 21, 22, 26, 27, 28, 35, 36])     # 去除Li, Be, B, K, Al, Na, Si, Ca, Sr, Ge, Y, Ag, Cd, In, Au (最佳)
# df = df.drop(index = [0, 1, 2, 3, 6, 7, 8, 21, 22, 28])     # 去除Li, Be, B,  K, Si, Na, Ca, Sr, Y, In(最合理)
# df = df.drop(index = [0, 1, 3, 7, 8, 21, 22])     # 去除Be, K, Ca, Sr, Y
# index = [3, 7, 8, 21, 22]
# for i in range(37):
#     if i not in index:
#         df = df.drop(index = [i])

df = (df.reset_index(drop=True))
#  =====================================================================================

ii = -1
for i, j in zip(df[col[0]].isna().tolist(), df[col[1]].isna().tolist() ):
    ii += 1
    if i == True or j == True:
        df = df.drop([ii])
    else: pass  # print(i, j)

# print(df['Element'])
# dict_element = df.to_dict()
# print(dict_element)

# elem_category ===========================================================================
elem_category = []
for eleNum in df['Atomic Number']:
    if eleNum in [3, 11, 19, 37, 55, 87]:
        elem_category.append('Alkali & alkaline earth')

    elif eleNum in [4, 12, 20, 38, 56, 88]:
        elem_category.append('Alkali & alkaline earth')

    elif eleNum in [1, 6, 7, 8, 9, 15, 16, 17, 34, 35, 53]:
        elem_category.append('Non Metal')

    elif eleNum in [2, 10, 18, 36, 54, 86]:
        elem_category.append('Inert')

    elif eleNum in [5, 14, 32, 33, 51, 52, 85]:
        elem_category.append('Metalloids')

    elif eleNum in [13, 31, 49, 50, 81, 82, 83, 84]:
        elem_category.append('Poor metal')

    elif eleNum in [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]:
        elem_category.append('Lanthanum')

    elif eleNum in [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]:
        elem_category.append('Actinide')

    else:
        elem_category.append('Metal')

df.insert(2, "Category", elem_category)
# 去除非金屬 ===========================================================================
# df = df.drop(df[(df['Metallic Radius']>=145)].index)
# df = df.drop(df[(df['Category']!='Metal') & (df['Category']!='Poor metal')].index)
df = df.drop(df[(df['Category']!='Metal')].index)
# df = df.drop(df[(df['Category']!='Alkali & alkaline earth')].index)
# df = df.drop(index = [22])     # 去除Be, K, Ca, Sr, Y

# Correlation Analysis ===========================================================================
x = df[col[0]].tolist()
x = np.vstack((x, df[col[1]].tolist()))
x = np.vstack((x, df[col[2]].tolist()))
x = np.vstack((x, df[col[3]].tolist()))
rho = np.corrcoef(x)

df[col[0]] = df[col[0]].astype(float, errors = 'raise')
# d_list ===========================================================================
d_list  = df.to_dict('list')
print(d_list)
plot_data = {}
for i, j in zip(d_list['Element'], d_list['Segregation energy (eV/lattice)']):
    # print(i, j)
    plot_data.update({i: float(j)} )

# # Figure ===========================================================================
# sns.set_style('darkgrid')
# fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))
#
# for i in [0,1,2]:
#     sns.scatterplot(x=col[0], y=col[1+i], hue='Category', data=df, s=50 , ax=ax[i]).set(title='Correlation = ' + "{:.2f}".format(rho[0,i+1]));
#     # sns.lmplot(x=col[0], y=col[1+i], data = df, hue='Category')
#     for ele, m, l in zip(df['Element'], df[col[0]], df[col[1+i]]):
#         ax[i].text(m+0.025, l+0.025, ele, fontsize=16)
# fig.subplots_adjust(wspace=.4)
# plt.tight_layout()
# plt.show()

# Figure ===========================================================================
sns.set_style('darkgrid')
sns.set_style('ticks')
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 8))

for i in [0,1,2]:
    g = sns.kdeplot(x=col[i], y=col[3], data=df, hue='Structure', thresh=0.05, ax=ax[i], alpha  = 0.1)
    g = sns.scatterplot(x=col[i], y=col[3], hue='Structure', data=df, s=75 , ax=ax[i]);
    ax[i].axes.set_title('Pearson Correlation = ' + "{:.2f}".format(rho[i, 3]), fontsize=20)
    g.set_xlabel(col[i], fontsize=20)
    g.set_ylabel(col[3], fontsize=20)
    # ax[i].set_xlim(110, 190)
    # ax[i].set_ylim(-1, 3.5)
    sns.move_legend(g, "lower right", title='Structure', fontsize='x-large', title_fontsize='20')
    #sns.scatterplot(x=col[0], y=col[1+i], hue='Structure', data=df, s=50, ax=ax[i+3]).set(title='Correlation = ' + "{:.2f}".format(rho[0,i+3]));
    # sns.lmplot(x=col[0], y=col[1+i], data = df, hue='Category')
    for ele, m, l in zip(df['Element'], df[col[i]], df[col[3]]):
        ax[i].text(m+0.04, l+0.04, ele, fontsize=16)

fig.subplots_adjust(wspace=.4)
plt.tight_layout()

# Figure ===========================================================================
df_BCC = df.drop(df[(df['Structure']!='BCC')].index)
df_FCC = df.drop(df[(df['Structure']!='FCC')].index)
df_HCP = df.drop(df[(df['Structure']!='HCP')].index)
x_BCC = np.vstack(( df_BCC[col[0]].tolist(), df_BCC[col[2]].tolist() ))
x_FCC = np.vstack(( df_FCC[col[0]].tolist(), df_FCC[col[2]].tolist() ))
x_HCP = np.vstack(( df_HCP[col[0]].tolist(), df_HCP[col[2]].tolist() ))
rho_BCC = np.corrcoef(x_BCC)
rho_FCC = np.corrcoef(x_FCC)
rho_HCP = np.corrcoef(x_HCP)
print(rho_BCC)
print(rho_FCC)
print(rho_HCP)
# sns.set_style('darkgrid')
sns.set_style('ticks')
sns.set(style='ticks', font='sans-serif', font_scale=2, rc=None)
gg = sns.lmplot(hue='Structure', x=col[0], y=col[3], data=df, height=8, aspect=1.15, facet_kws={'legend_out': False}).set(title='Pearson Correlation = ' + "{:.2f}".format(rho[0,3]))
gg.set_axis_labels(x_var='Metallic Radius (pm)', fontsize = 25)
gg.set_axis_labels(y_var='Segregation energy (eV/lattice)', fontsize = 30)
# gg.set_xlabel('Metallic Radius (pm)', fontsize=20)
# gg.set_ylabel('Segregation energy (eV/lattice)', fontsize=20)
# gg.set(ylim=(-1, 3.5))
# gg.set(xlim=(120, 185))
# check axes and find which is have legend
leg = gg.axes.flat[0].get_legend()
new_title = 'Structure'
leg.set_title(new_title)
new_labels = ['HCP', 'BCC', 'FCC']
for t, l in zip(leg.texts, new_labels):
    t.set_text(l)

# sns.move_legend(gg, "lower right", title='Structure', fontsize='10', title_fontsize='14')
sns.despine(top=False, right=False, bottom=False, left=False)
for ele, m, l in zip(df['Element'], df[col[0]], df[col[3]]):
        plt.text(m+0.025, l+0.025, ele, fontsize=16)

plt.text(130, -1, 'Pearson Correlation of FCC = ' + "{:.2f}".format(rho_FCC[0,1]), fontsize=18, color='g')
plt.text(150, 0.88, 'Pearson Correlation of HCP = ' + "{:.2f}".format(rho_HCP[0,1]), fontsize=18, color='dodgerblue')
plt.text(123, 2.75, 'Pearson Correlation of BCC = ' + "{:.2f}".format(rho_BCC[0,1]), fontsize=18, color='chocolate')
plt.tight_layout()
# plt.show()


# Plot elemTable ===========================================================================
# Plot elemTable ===========================================================================
sns.set(style='ticks', font='sans-serif', font_scale=1, rc=None)
print(plot_data)
print(len(plot_data))
polt_elemTable(plot_data)
