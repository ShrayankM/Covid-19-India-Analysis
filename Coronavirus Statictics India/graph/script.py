import numpy as np
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

import math

# from matplotlib import style

import urllib.request
import json

from pathlib import Path
import os

import warnings
warnings.filterwarnings("ignore")

url = "https://api.covid19india.org/states_daily.json"
# from graph import models

def make_data():
    with open('data.json') as f:
        data = json.load(f)
    data = data['states_daily']
    df = pd.json_normalize(data)
    return df

# def create_pie_chart(df, dir):
#     df_pie = df[['status', 'tt']]
#     df_pie['tt'] = pd.to_numeric(df_pie['tt'])
#     pie_data = []
#     for i in df['status'].unique():
#         pie_data.append(df_pie[df_pie['status'] == i]['tt'].sum())
#     pie_data[0] = pie_data[0] - (pie_data[1] + pie_data[2])
#     plt.clf()
#     cmap = plt.get_cmap('tab10')
#     my_colors = cmap(np.array([1, 2, 3]))
#     plt.pie(pie_data, labels = df['status'].unique(), autopct = "%.2f%%",
#             radius = 1.3, shadow = True, startangle = 180,
#             colors = my_colors, wedgeprops = dict(width = 0.4), pctdistance = 0.5,
#             textprops = {'fontsize' : 17, 'fontweight' : 'bold'});
#     path = os.path.join(dir, 'images')
#     plt.savefig(os.path.join(path, 'pie.jpg'), orientation = {'portrait'}, bbox_inches = 'tight')

def create_pie_chart(df, dir, tdir):
    df_pie = df[['status', 'tt']]
    df_pie['tt'] = pd.to_numeric(df_pie['tt'])
    df_g = df_pie.groupby('status', as_index = False).sum()
    df_g.loc[0, 'tt'] -= df_g.loc[1, 'tt']
    df_g.loc[0, 'tt'] -= df_g.loc[2, 'tt']
    df_g.loc[0, 'status'] = 'Active'
    colors = []
    colors.append(px.colors.qualitative.G10[2])
    colors.append(px.colors.qualitative.G10[1])
    colors.append(px.colors.qualitative.G10[3])

    fig = go.Figure(data=[go.Pie(labels=['Active', 'Deceased', 'Recovered'],
                                 values=df_g['tt'], pull=[0, 0, 0], rotation = 180,
                                 title = {'text' : 'Recovery Rate India',  'position' : 'top left',
                                          'font': {'size' : 20}},
                                 showlegend = True)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15,
                      marker=dict(colors=colors, line=dict(color='#000000', width=1)))
    fig.update_layout(
        paper_bgcolor="LightSteelBlue",
        margin=dict(
            l=0,
            r=0,
            b=50,
            t=50,
            pad=0
        ),
        hoverlabel=dict(
            font_family='serif',
            font_size=18,
        ),
    )
    fig.update_yaxes(automargin = True)
    fig.update_xaxes(automargin = True)
    pio.write_html(fig, file= os.path.join(tdir, 'graph/pie_chart.html'), auto_open=False)

# def create_line_chart(df, dir):
#     df_ = df.copy(deep = True)
#     df_['date'] = pd.to_datetime(df_['date'])
#     df_ = df_[['date', 'status', 'tt']]
#     df_['Cases'] = pd.to_numeric(df_['tt'])
#     cmap = plt.get_cmap('tab10')
#     my_colors = cmap(np.array([1, 2, 3]))
#     plt.clf()
#     fig = plt.gcf()
#     fig.set_size_inches(15, 6)
#     svm = sns.lineplot('date', 'Cases', data = df_,
#                  hue = 'status', ci = 95,
#                  palette = {'Confirmed':my_colors[0], 'Recovered':my_colors[1], 'Deceased':my_colors[2]});
#     path = os.path.join(dir, 'images')
#     figure = svm.get_figure()
#     figure.savefig(os.path.join(path, 'area.jpg'), bbox_inches = 'tight')
#     plt.xticks(rotation = 45);

def create_line_chart(df, dir, tdir):
    df_ = df.copy(deep = True)
    df_['date'] = pd.to_datetime(df_['date'])
    df_ = df_[['date', 'status', 'tt']]
    df_['Cases'] = pd.to_numeric(df_['tt'])
    df_conf = df_[df_['status'] == 'Confirmed']
    df_rec  = df_[df_['status'] == 'Recovered']
    df_dec  = df_[df_['status'] == 'Deceased']
    colors = []
    colors.append(px.colors.qualitative.G10[2])
    colors.append(px.colors.qualitative.G10[1])
    colors.append(px.colors.qualitative.G10[3])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x= df_conf['date'], y = df_conf['tt'],
                             mode='markers',
                             marker=dict(
                             color='#F69A30',
                             line=dict(
                                color='black',
                                width=0.2
                             )),
                             name="Confirmed", line_shape='spline',))
    fig.add_trace(go.Scatter(x= df_rec['date'], y = df_rec['tt'],
                             mode='markers',
                             marker=dict(
                             color='#387938',
                             line=dict(
                                color='black',
                                width=0.2
                             )),
                             name="Recovered", line_shape='spline'))
    fig.add_trace(go.Scatter(x= df_dec['date'], y = df_dec['tt'],
                             mode='markers',
                             marker=dict(
                             color='#B2322B',
                             line=dict(
                                color='black',
                                width=0.2
                             )),
                             name="Deceased", line_shape='spline'))

    fig.update_traces(hoverinfo='text+y+x', mode='lines+markers')
    fig.update_layout(
        xaxis_title = 'Months',
        yaxis_title = 'Cases',
        title = {
           'text': "Overall Cases in India",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        legend=dict(x=0.01,y=0.9, traceorder='reversed', font_size=16),
        margin=dict(
            l=0,
            r=0,
            b=20,
            t=10,
            pad=0
        ),)

    # fig.show()
    fig.update_yaxes(automargin = True)
    fig.update_xaxes(automargin = True)
    pio.write_html(fig, file= os.path.join(tdir, 'graph/area_chart.html'), auto_open=False)

def create_dataset(df):
    df_bar = df.tail(3)
    df_bar.set_index('status', inplace = True)
    df_bar.drop('date', axis = 1, inplace = True)
    df_bar.drop('tt', axis = 1, inplace = True)
    df_bar.drop('un', axis = 1, inplace = True)
    df_bar.drop('dateymd', axis = 1, inplace = True)
    df_bar = df_bar.apply(pd.to_numeric)
    df_bar = df_bar.T
    return df_bar

def overall_info(df):
    df_states = df.copy(deep = True)
    df_states['date'] = pd.to_datetime(df_states['date'])
    df_states.drop('tt', axis = 1, inplace = True)
    df_states.drop('dateymd', axis = 1, inplace = True)
    ########## ALL States Confirmed Data #############################
    df_C = df_states[df_states['status'] == 'Confirmed'].copy(deep = True)
    df_C.drop('status', axis = 1, inplace = True)
    df_MC = pd.melt(df_C, id_vars = 'date', value_vars = list(df_C.columns).remove('date'),
                var_name = 'state', value_name = 'Confirmed')
    df_MC['Confirmed'] = pd.to_numeric(df_MC['Confirmed'])
    df_MC.drop('date', axis = 1, inplace = True)
    df_MC = df_MC.groupby('state').sum()
    df_MC = df_MC['Confirmed']
    ##################################################################
    ########## ALL States Recovered Data #############################
    df_R = df_states[df_states['status'] == 'Recovered'].copy(deep = True)
    df_R.drop('status', axis = 1, inplace = True)
    df_MR = pd.melt(df_R, id_vars = 'date', value_vars = list(df_R.columns).remove('date'),
                var_name = 'state', value_name = 'Recovered')
    df_MR['Recovered'] = pd.to_numeric(df_MR['Recovered'])
    df_MR.drop('date', axis = 1, inplace = True)
    df_MR = df_MR.groupby('state').sum()
    df_MR = df_MR['Recovered']
    ##################################################################
    ########## ALL States Deceased Data ##############################
    df_D = df_states[df_states['status'] == 'Deceased'].copy(deep = True)
    df_D.drop('status', axis = 1, inplace = True)
    df_MD = pd.melt(df_D, id_vars = 'date', value_vars = list(df_D.columns).remove('date'),
                var_name = 'state', value_name = 'Deceased')
    df_MD['Deceased'] = pd.to_numeric(df_MD['Deceased'])
    df_MD.drop('date', axis = 1, inplace = True)
    df_MD = df_MD.groupby('state').sum()
    df_MD = df_MD['Deceased']
    ##################################################################
    return df_MC, df_MR, df_MD
state_dict = {
    'AP' : 'Andhra Pradesh',
    'AR' : 'Arunanchal Pradesh',
	'AS' : 'Assam',
	'BR' : 'Bihar',
	'CT' : 'Chhattisgarh',
	'GA' : 'Goa',
	'GJ' : 'Gujarat',
 	'HR' : 'Haryana',
	'HP' : 'Himachal Pradesh',
	'JH' : 'Jharkhand',
	'KA' : 'Karnataka',
	'KL' : 'Kerala',
	'MP' : 'Madhya Pradesh',
	'MH' : 'Maharashtra',
	'MN' : 'Manipur',
	'ML' : 'Meghalaya',
	'MZ' : 'Mizoram',
	'NL' : 'Nagaland',
	'OR' : 'Odisha',
	'PB' : 'Punjab',
	'RJ' : 'Rajasthan',
	'SK' : 'Sikkim',
	'TN' : 'Tamil Nadu',
	'TR' : 'Tripura',
	'UP' : 'Uttar Pradesh',
	'UT' : 'Uttarakhand',
	'WB' : 'West Bengal',
	'TG' : 'Telangana',
	'AN' : 'Andaman & Nicobar Island',
	'CH' : 'Chandigarh',
	'DN' : 'Dadara & Nagar Havelli',
	'DD' : 'Daman & Diu',
	'JK' : 'Jammu & Kashmir',
	'LA' : 'Ladakh',
	'LD' : 'Lakshadweep',
	'DL' : 'NCT of Delhi',
	'PY' : 'Puducherry' 
}

def update_state_name(state):
    state = state.upper()
    return state_dict[state]

def getForStatus(data, status_value):
    df = data[data['status'] == status_value].copy(deep = True)
    df.drop('status', axis = 1, inplace = True)
    df.drop('tt', axis = 1, inplace = True)
    df.drop('un', axis = 1, inplace = True)
    temp_date = df['dateymd']
    df.drop('dateymd', axis = 1, inplace = True)
    df = df.apply(pd.to_numeric)
    df['dateymd'] = pd.to_datetime(temp_date)

    df = pd.melt(df, id_vars = 'dateymd', 
                         value_vars = list(df.columns).remove('dateymd'), 
                         var_name = 'state', value_name = status_value)
    df = df.groupby('state').sum()

    df['state_name'] = [update_state_name(x) for x in df.index]
    return df

def return_arr(df, status):
    arr = []
    for x, y in df.iterrows():
        arr.append(y['state_name'] + " (" + str(y[status]) + ")")
    return arr

def generate_table(data):
    data.drop('date', axis = 1, inplace = True)
    today_data = data.tail(3)
    data = today_data.copy(deep = True)
    today_confirmed = getForStatus(data, "Confirmed")
    today_recovered = getForStatus(data, "Recovered")
    today_deceased = getForStatus(data, "Deceased")

    today_confirmed.sort_values('Confirmed', ascending = False, inplace = True)
    today_recovered.sort_values('Recovered', ascending = False, inplace = True)
    today_deceased.sort_values('Deceased', ascending = False, inplace = True)

    today_confirmed_top = today_confirmed.head(5)
    today_recovered_top = today_recovered.head(5)
    today_deceased_top = today_deceased.head(5)

    conf_arr = return_arr(today_confirmed_top, 'Confirmed')
    reco_arr = return_arr(today_recovered_top, 'Recovered')
    dece_arr = return_arr(today_deceased_top, 'Deceased')

    tabular_dataframe = {'Confirmed': conf_arr, 'Recovered': reco_arr, 'Deceased': dece_arr}
    df = pd.DataFrame(data = tabular_dataframe)
    return df

def append_count(df, type):
    return df[type].sum()

def get_percentage(total, value):
    return round((value/total) * 100, 2)

def percentage_info(data):

    # today_data = data.tail(3)
    # count_today = np.array(today_data['tt'], dtype=int)

    data_confirmed = getForStatus(data, 'Confirmed')
    data_recovered = getForStatus(data, 'Recovered')
    data_deceased = getForStatus(data, 'Deceased')

    count_arr = []
    count_arr.append(append_count(data_confirmed, 'Confirmed'));
    count_arr.append(append_count(data_recovered, 'Recovered'));
    count_arr.append(append_count(data_deceased, 'Deceased'));

    count_arr[0] = count_arr[0] - count_arr[1]
    count_arr[0] = count_arr[0] - count_arr[2]
    total_cnt = 0

    for x in count_arr:
        total_cnt += x

    print(count_arr)

    count_arr = [get_percentage(total_cnt, x) for x in count_arr]
    # count_today = [get_percentage(np.sum(count_today), x) for x in count_today]
    return count_arr


def start():
    urllib.request.urlretrieve(url, 'data.json');
    df = make_data()

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # create_pie_chart(df, STATIC_DIR, TEMPLATE_DIR)
    create_line_chart(df, STATIC_DIR, TEMPLATE_DIR)
    df_bar = create_dataset(df)
    df_MC, df_MR, df_MD = overall_info(df)
    df_table = generate_table(df)
    df_perc = percentage_info(df)
    return df_bar, df_MC, df_MR, df_MD, df_table, df_perc

start()
# if __name__ == '__main__':
#     start()
