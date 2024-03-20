

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 25)

import seaborn as sns
import matplotlib.pyplot as plt

data_df = pd.read_csv('Bias_correction_ucl.csv', index_col='Date', parse_dates=True)


data_df.reset_index(inplace=True)
data_df['Year']  = data_df['Date'].dt.year
data_df['Month'] = data_df['Date'].dt.month
data_df['Day']   = data_df['Date'].dt.day
data_df.set_index('Date', inplace=True)

print('Getting the info: ')
print(data_df.info())

print('The stats of the data: ')
print(data_df.describe())


data_df.drop(data_df.tail(2).index, inplace=True)
index_present_tmax= data_df['Present_Tmax'].index[data_df['Present_Tmax'].apply(np.isnan)]
index_present_tmin= data_df['Present_Tmin'].index[data_df['Present_Tmin'].apply(np.isnan)]

index_next_tmax   = data_df['Next_Tmax'].index[data_df['Next_Tmax'].apply(np.isnan)]
index_next_tmin   = data_df['Next_Tmin'].index[data_df['Next_Tmin'].apply(np.isnan)]

index_LDAPS_RHmax = data_df['LDAPS_RHmax'].index[data_df['LDAPS_RHmax'].apply(np.isnan)]
index_LDAPS_RHmin = data_df['LDAPS_RHmin'].index[data_df['LDAPS_RHmin'].apply(np.isnan)]
index_Tmax_lapse  = data_df['LDAPS_Tmax_lapse'].index[data_df['LDAPS_Tmax_lapse'].apply(np.isnan)]
index_Tmin_lapse  = data_df['LDAPS_Tmin_lapse'].index[data_df['LDAPS_Tmin_lapse'].apply(np.isnan)]
index_LDAPS_WS    = data_df['LDAPS_WS'].index[data_df['LDAPS_WS'].apply(np.isnan)]
index_LDAPS_LH    = data_df['LDAPS_LH'].index[data_df['LDAPS_LH'].apply(np.isnan)]
index_LDAPS_CC1   = data_df['LDAPS_CC1'].index[data_df['LDAPS_CC1'].apply(np.isnan)]
index_LDAPS_CC2   = data_df['LDAPS_CC2'].index[data_df['LDAPS_CC2'].apply(np.isnan)]
index_LDAPS_CC3   = data_df['LDAPS_CC3'].index[data_df['LDAPS_CC3'].apply(np.isnan)]
index_LDAPS_CC4   = data_df['LDAPS_CC4'].index[data_df['LDAPS_CC4'].apply(np.isnan)]
index_LDAPS_PPT1  = data_df['LDAPS_PPT1'].index[data_df['LDAPS_PPT1'].apply(np.isnan)]
index_LDAPS_PPT2  = data_df['LDAPS_PPT2'].index[data_df['LDAPS_PPT2'].apply(np.isnan)]
index_LDAPS_PPT3  = data_df['LDAPS_PPT3'].index[data_df['LDAPS_PPT3'].apply(np.isnan)]
index_LDAPS_PPT4  = data_df['LDAPS_PPT4'].index[data_df['LDAPS_PPT4'].apply(np.isnan)]

if list(index_present_tmax) == list(index_present_tmin):
    print('Lists are identical')
else: print('Unidentical lists')

if list(index_next_tmax) == list(index_next_tmin):
    print('Lists are identical')
else: print('Unidentical lists')
        
if list(index_LDAPS_RHmax)==list(index_LDAPS_RHmin)==list(index_Tmax_lapse)==list(index_Tmin_lapse)==list(index_LDAPS_WS)==list(index_LDAPS_LH)==list(index_LDAPS_CC1)==list(index_LDAPS_CC2)==list(index_LDAPS_CC3)==list(index_LDAPS_CC4)==list(index_LDAPS_PPT1)==list(index_LDAPS_PPT2)==list(index_LDAPS_PPT3)==list(index_LDAPS_PPT4):
    print('Lists are identical')
else: print('Unidentical lists')
no_of_stations = 25
station = [[] for _ in range(no_of_stations+1)]

for i in range(1,len(station)):
    station[i] = data_df.loc[data_df['station'] == i]
for i in range(1,len(station)):
    station[i] = station[i].fillna(station[i].mean())
    #station[i].set_index('Date', inplace=True)
new_data = pd.DataFrame(columns=['lat','lon'], index=range(0,25))
for i in range(0,25):
    new_data['lat'][i] = data_df['lat'][i]
    new_data['lon'][i] = data_df['lon'][i]
    
fig, ax = plt.subplots()
ax.scatter(new_data['lat'],new_data['lon'], alpha=0.5)
plt.title('Geographical location of stations')

labels = [i for i in range(1,len(station))]
for i, txt in enumerate(labels):
    ax.annotate(txt, (new_data['lat'][i],new_data['lon'][i]))

for i in range(1,len(station)):

    plt.rcParams.update({'font.size': 5})
    ncols = 2
    nrows = 2
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    fig.suptitle('Next Max temp at station {}'.format(i))
    years = [2013,2014,2015,2016]
    
    for ax, j in zip(axes.flatten(), years):
        ax.plot(station[i].loc[station[i]['Year']==j]['Next_Tmax'], linewidth=0.75)
        ax.title.set_text('Year {}'.format(j))
    
    for ax in axes.flatten():
        ax.set_xticks([])
        ax.tick_params(axis='y', labelsize=5)        

years = [2013,2014,2015,2016]
for j in years:
    
    plt.rcParams.update({'font.size:5'})
    ncols = 5
    nrows = 5
    
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols)
    fig.suptitle('Year {}'.format(j))
    i = range(1,26)
    
    for ax, i in zip(axes.flatten(), i):
        ax.plot(station[i].loc[station[i]['Year']==j]['Next_Tmax'], linewidth=0.75)
        ax.title.set_text('Station {}'.format(i))
        
    for ax in axes.flatten():
        ax.set_xticks([])
        ax.tick_params(axis='y', labelsize=5)
    
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.tight_layout()
    
