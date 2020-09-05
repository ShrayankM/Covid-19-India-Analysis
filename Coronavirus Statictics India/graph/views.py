from django.shortcuts import render
from graph import script
from django.views.decorators.clickjacking import xframe_options_sameorigin

# from graph.models import StateInfo
state_dict = {
    'AP' : 'Andhra Pradesh',
    'AR' : 'Arunachal Pradesh',
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
	'UT' : 'Uttarakhanad',
	'WB' : 'West Bengal',
	'TG' : 'Telangana',
	'AN' : 'Andaman and Nicobar Islands',
	'CH' : 'Chandigarh',
	'DN' : 'Dadra and nagar Haveli',
	'DD' : 'Daman and Diu',
	'JK' : 'Jammu and Kashmir',
	'LA' : 'Ladakh',
	'LD' : 'Lakshadweep',
	'DL' : 'Delhi',
	'PY' : 'Puducherry' }

class State:
    def __init__(self, name, c, r, d, tc, tr, td):
        self.name = name
        self.c = c
        self.r = r
        self.d = d
        self.tc = tc
        self.tr = tr
        self.td = td


def insert_data(df, c, r, d):
    state_list = []
    total_list = [0, 0, 0]
    today_total = [0, 0, 0]
    for index, row in df.iterrows():
        state_list.append(State(state_dict[str(index).upper()], row['Confirmed'],
                          row['Recovered'], row['Deceased'], c.get(key = index),
                          r.get(key = index), d.get(key = index)))

        today_total[0] += row['Confirmed']
        today_total[1] += row['Recovered']
        today_total[2] += row['Deceased']

        total_list[0] += c.get(key = index)
        total_list[1] += r.get(key = index)
        total_list[2] += d.get(key = index)
    return state_list, total_list, today_total



def temp(request):
    [df, df_MC, df_MR, df_MD] = script.start()
    state_list, total_list, today_total = insert_data(df, df_MC, df_MR, df_MD)
    # total_list = tInfo(df, df_MC, df_MR, df_MD)
    # print(total_list)
    my_dict = {'state_table' : state_list, 'overall_list' : total_list, 'today_t' : today_total}
    return render(request, 'graph/temp.html', context = my_dict)


def pie(request):
    return render(request, 'graph/pie_chart.html')

def area(request):
    return render(request, 'graph/area_chart.html')
