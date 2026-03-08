#v01:  07/03/26, for github and stlit CC
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import fvz_industries_v01 as fvz
import industries_data_020326 as indata

#-----------------------------------------------------------------------

A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12,A13,A14 = fvz.A01,fvz.A02,fvz.A03,fvz.A04,fvz.A05,fvz.A06,fvz.A07,fvz.A08,fvz.A09,fvz.A10,fvz.A11,fvz.A12,fvz.A13,fvz.A14
B01,B02,B03,B04,B05,B06,B07 = fvz.B01,fvz.B02,fvz.B03,fvz.B04,fvz.B05,fvz.B06,fvz.B07
C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23 = fvz.C01,fvz.C02,fvz.C03,fvz.C04,fvz.C05,fvz.C06,fvz.C07,fvz.C08,fvz.C09,fvz.C10,fvz.C11,fvz.C12,fvz.C13,fvz.C14,fvz.C15,fvz.C16,fvz.C17,fvz.C18,fvz.C19,fvz.C20,fvz.C21,fvz.C22,fvz.C23
D01,D02,D03,D04,D05,D06,D07,D08,D09,D10,D11,D12 = fvz.D01,fvz.D02,fvz.D03,fvz.D04,fvz.D05,fvz.D06,fvz.D07,fvz.D08,fvz.D09,fvz.D10,fvz.D11,fvz.D12
E01,E02,E03,E04,E05,E06,E07,E08 = fvz.E01,fvz.E02,fvz.E03,fvz.E04,fvz.E05,fvz.E06,fvz.E07,fvz.E08
F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15 = fvz.F01,fvz.F02,fvz.F03,fvz.F04,fvz.F05,fvz.F06,fvz.F07,fvz.F08,fvz.F09,fvz.F10,fvz.F11,fvz.F12,fvz.F13,fvz.F14,fvz.F15
G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11 = fvz.G01,fvz.G02,fvz.G03,fvz.G04,fvz.G05,fvz.G06,fvz.G07,fvz.G08,fvz.G09,fvz.G10,fvz.G11
H01,H02,H03,H04,H05,H06,H07,H08,H09,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,H24,H25 = fvz.H01,fvz.H02,fvz.H03,fvz.H04,fvz.H05,fvz.H06,fvz.H07,fvz.H08,fvz.H09,fvz.H10,fvz.H11,fvz.H12,fvz.H13,fvz.H14,fvz.H15,fvz.H16,fvz.H17,fvz.H18,fvz.H19,fvz.H20,fvz.H21,fvz.H22,fvz.H23,fvz.H24,fvz.H25
I01,I02,I03,I04,I05,I06,I07,I08,I09,I10,I11,I12 = fvz.I01,fvz.I02,fvz.I03,fvz.I04,fvz.I05,fvz.I06,fvz.I07,fvz.I08,fvz.I09,fvz.I10,fvz.I11,fvz.I12
J01,J02,J03,J04,J05,J06,J07,J08,J09,J10,J11,J12 = fvz.J01,fvz.J02,fvz.J03,fvz.J04,fvz.J05,fvz.J06,fvz.J07,fvz.J08,fvz.J09,fvz.J10,fvz.J11,fvz.J12
K01,K02,K03,K04,K05,K06 = fvz.K01,fvz.K02,fvz.K03,fvz.K04,fvz.K05,fvz.K06


allindus = [A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12,A13,A14,
            B01,B02,B03,B04,B05,B06,B07,
            C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,
            D01,D02,D03,D04,D05,D06,D07,D08,D09,D10,D11,D12,
            E01,E02,E03,E04,E05,E06,E07,E08,
            F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15,
            G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11,
            H01,H02,H03,H04,H05,H06,H07,H08,H09,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,H24,H25,
            I01,I02,I03,I04,I05,I06,I07,I08,I09,I10,I11,I12,
            J01,J02,J03,J04,J05,J06,J07,J08,J09,J10,J11,J12,
            K01,K02,K03,K04,K05,K06]

dic_sectors = {'Basic Materials':[A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12,A13,A14],
            'Communication Services':[B01,B02,B03,B04,B05,B06,B07],
            'Consumer Cyclical':[C01,C02,C03,C04,C05,C06,C07,C08,C09,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23],
            'Consumer Defensive':[D01,D02,D03,D04,D05,D06,D07,D08,D09,D10,D11,D12],
            'Energy':[E01,E02,E03,E04,E05,E06,E07,E08],
            'Financial':[F01,F02,F03,F04,F05,F06,F07,F08,F09,F10,F11,F12,F13,F14,F15],
            'Healthcare':[G01,G02,G03,G04,G05,G06,G07,G08,G09,G10,G11],
            'Industrials':[H01,H02,H03,H04,H05,H06,H07,H08,H09,H10,H11,H12,H13,H14,H15,H16,H17,H18,H19,H20,H21,H22,H23,H24,H25],
            'Real Estate':[I01,I02,I03,I04,I05,I06,I07,I08,I09,I10,I11,I12],
            'Technology':[J01,J02,J03,J04,J05,J06,J07,J08,J09,J10,J11,J12],
            'Utilities':[K01,K02,K03,K04,K05,K06]}

#================================
hist_dates00 = ['2022-10-13','2023-07-27','2023-10-27','2024-07-16','2024-08-05','2025-02-19','2025-04-07','2025-10-09','2025-11-20','2026-01-28']
hist_dates00a = ['2022-10-13','2023-7-27','2023-10-27','2024-7-16','2024-8-5','2025-2-19','2025-4-7','2025-10-9','2025-11-20','2026-1-28']
hist_dates01 = ['13/oct/22', '27/jul/23', '27/oct/23', '16/jul/24', '05/aug/24', '19/feb/25', '07/apr/25', '09/oct/25', '20/nov/25', '28/jan/26']
hist_dates02 = [f"({i+1}) {x}" for i,x in enumerate(hist_dates01)]

dat_refs = indata.DHisto_dat[-1]  #last values stored (price, mktcap)
#--------------------------------\/
#calc and store mkt cap by sector:
Sect_ind_mkcaps = []
Sectors_mkcaps = {}
for k,v in dic_sectors.items():
    for gro in v:
        sumag = 0
        for sto in gro:
            try:
                sumag += dat_refs[sto][1]
            except:
                print(f"not for {sto}")
                continue            
        gro_name = fvz.indus_names(gro)
        Sect_ind_mkcaps.append((k, gro_name, round(sumag,2)))
        
for s in fvz.lis_sectors:
    temp = [x[2] for x in Sect_ind_mkcaps if x[0] == s]
    Sectors_mkcaps[s] = round(sum(temp),2)
#--------------------------------/\
def dates_delta_abs(d01, d02):
    ds_12 = []
    
    for d in [d01, d02]:
        for i in range(len(hist_dates01)):
            if d == hist_dates01[i]:  #'16/jul/24'
                dt = hist_dates00a[i]   #'2024-7-16'
                break
        temp = dt.split('-')  #['2024', '7', '16']
        ds_12.append(datetime(int(temp[0]),int(temp[1]),int(temp[2])))

    d_user = relativedelta(ds_12[1], ds_12[0])

    if d_user.years >= 1:
        return f"{round(d_user.years + d_user.months/12 + d_user.days/365, 1)} years"
    else:
        return f"{round(d_user.months + d_user.days/30, 1)} months"
        
def sector_evaluate(secs, dt_rfs, date1, date2):
    for i, x in enumerate(hist_dates01):
        if date1 == x:
            dat_date1 = indata.DHisto_dat[i]
        if date2 == x:
            dat_date2 = indata.DHisto_dat[i]

    if '*Select all sectors' in secs:        
        secs = fvz.lis_sectors
        
    Sec_res = []
    for sec in secs:
        BRes = []
        BRes_disp = []        
        for gro in dic_sectors[sec]:
            Gro_res = []
            for sto in gro:
                try:
                    #calc delta:
                    delta = round((dat_date2[sto] - dat_date1[sto]) / dat_date1[sto], 4)
                    if sto != 'SPY':
                        Gro_res.append((sto, delta, (dat_refs[sto][1]/dat_refs[sto][0])*dat_date2[sto]))
                                      #(sto, delta, app. mktcap date2)
                except:
                    continue

            if gro != ['SPY']:        
                gro_name = fvz.indus_names(gro)
            else:
                gro_name = '---'
            BRes.append((gro_name, Gro_res))

        for j in range(0, len(BRes)):      
            try:
                sum_mcap_d2 = sum([x[2] for x in BRes[j][1]])
                delta_gro = round(sum([x[1]*(x[2]/sum_mcap_d2) for x in BRes[j][1]]), 4)
                BRes_disp.append((BRes[j][0], delta_gro, sum_mcap_d2))
            except:
                continue
        delta_sec = 0
        for k in range(0, len(BRes_disp)):
            delta_sec += BRes_disp[k][1]*(BRes_disp[k][2]/Sectors_mkcaps[sec])
        Sec_res.append((sec, round(delta_sec, 4)))

    #add SPY:
    Sec_res.append(('SPY', round((dat_date2['SPY'] - dat_date1['SPY']) / dat_date1['SPY'], 4)))
    Sec_res = sorted(Sec_res, key=lambda x:x[1], reverse=True)  #ordering for perfo

    Sec_res2 = []
    #correcting decimals:
    for x in Sec_res:
        bb = str(x[1]*100)
        Sec_res2.append((x[0], bb[:bb.index('.')+3]+'%'))

    st.divider()
    st.write(f"from {date1} to {date2}  (time: {dates_delta_abs(date1, date2)}):")

    #table with results: 
    Sec_res2_df = pd.DataFrame(Sec_res2,columns=['Sector','Performance'])
    st.dataframe(Sec_res2_df, width="content", hide_index=True)

    #st chart:
    Sec_res_df = pd.DataFrame(Sec_res,columns=['Sector','Performance'])

    clrs_data = (alt.when(alt.datum.Sector == 'SPY')
        .then(alt.value('orange'))      #specific category
        .when(alt.datum.Performance < 0)
        .then(alt.value('red'))         #negative values
        .otherwise(alt.value('lightblue')))

    if Sec_res[-1][1] <= -0.50:
        x_left = -3.00
    elif Sec_res[-1][1] > -0.50 and Sec_res[-1][1] <= 0:
        x_left = -2.00
    elif Sec_res[-1][1] > 0:
        x_left = -1.00

    if Sec_res[0][1] <= -0.50:
        x_right = 0.50
    elif Sec_res[0][1] > -0.50 and Sec_res[0][1] <= 1:
        x_right = 2.00
    elif Sec_res[0][1] > 1:
        x_right = 3.00
    
    dom_xmin = min(Sec_res[-1][1]*1.5, x_left) 
    dom_xmax = max(Sec_res[0][1]*1.1, x_right) 

    chart_Sec = (alt.Chart(Sec_res_df).mark_bar().encode(y=alt.Y('Sector:O',
                        sort='-x',axis=alt.Axis(labelAlign='left')),
                        x=alt.X('Performance:Q').scale(domain=[dom_xmin, dom_xmax]),
                                color=clrs_data).properties(height=700))

    st.altair_chart(chart_Sec,width="stretch",height="stretch")

#end of def sector_evaluate*****************************************
   
def indus_evaluate(indus, dt_rfs, date1, date2):

    for i, x in enumerate(hist_dates01):
        if date1 == x:
            dat_date1 = indata.DHisto_dat[i]
        if date2 == x:
            dat_date2 = indata.DHisto_dat[i]

    BRes = []
    BRes_disp = []
    for gro in indus:
        Res = []
        for sto in gro:
            try:
                #calc delta:
                delta = round((dat_date2[sto] - dat_date1[sto]) / dat_date1[sto], 4)
                if sto != 'SPY':
                    Res.append((sto, delta, (dt_rfs[sto][1]/dt_rfs[sto][0])*dat_date2[sto]))
                              #(sto, delta, app. mktcap date2)
                else:
                    Res.append((sto, delta))
            except:
                continue

        if gro != ['SPY']:        
            gro_name = (fvz.indus_names(gro))[4:]
        else:
            gro_name = '---'
        BRes.append((gro_name, Res))

    for j in range(1, len(BRes)):      #not including 1st (SPY)
        try:
            sum_mcap_d2 = sum([x[2] for x in BRes[j][1]])
            delta_gro = round(sum([x[1]*(x[2]/sum_mcap_d2) for x in BRes[j][1]]), 4)
            BRes_disp.append((BRes[j][0], delta_gro))
        except:
            continue

    BRes_disp.append(BRes[0][1][0])  #adding SPY
    BRes_disp = sorted(BRes_disp, key=lambda x:x[1], reverse=True)  #ordering for perfo
    BRes_disp2 = []
    
    #correcting decimals:
    for i,x in enumerate(BRes_disp):
        if i < 9:
            nn = f"00{i+1}"
        elif i < 99:
            nn = f"0{i+1}"
        else:
            nn = i+1
        bb = str(x[1]*100)
        if '.' in bb and x[0] != 'SPY':
            BRes_disp2.append((f"{nn}) {x[0]}", bb[:bb.index('.')+3]+'%'))    
        elif '.' in bb and x[0] == 'SPY':
            BRes_disp2.append((x[0], bb[:bb.index('.')+3]+'%'))    
        elif '.' not in bb and x[0] != 'SPY':
            BRes_disp2.append((f"{nn}) {x[0]}", bb +'%'))
        else:
            BRes_disp2.append((x[0], bb +'%'))

    st.divider()
    st.write(f"SPY vs Industries, from {date1} to {date2}  (time: {dates_delta_abs(date1, date2)}):")

    #table with results: 
    BRes_disp2_df = pd.DataFrame(BRes_disp2,columns=['Industry','Performance'])
    st.dataframe(BRes_disp2_df, width="content", hide_index=True)
    #--------
    BRes_disp3 = []     #idem to BRes_disp, but shorting inds names (to 'Steel')
    for i,x in enumerate(BRes_disp):
        if i < 9:
            nn = f"00{i+1}"
        elif i < 99:
            nn = f"0{i+1}"
        else:
            nn = i+1       
        if ' - ' in x[0]:
            BRes_disp3.append((f"{nn}) {x[0][x[0].index('-')+2:]}", x[1]))
        else:
            BRes_disp3.append(x)
    #--------

    #st chart:
    BRes_disp3_df = pd.DataFrame(BRes_disp3,columns=['Industry','Performance'])

    clrs_data = (alt.when(alt.datum.Industry == 'SPY')
        .then(alt.value('orange'))      #specific category
        .when(alt.datum.Performance < 0)
        .then(alt.value('red'))         #negative values
        .otherwise(alt.value('lightblue')))

    if BRes_disp3[-1][1] <= -0.50:
        x_left = -3.00
    elif BRes_disp3[-1][1] > -0.50 and BRes_disp3[-1][1] <= 0:
        x_left = -2.00
    elif BRes_disp3[-1][1] > 0:
        x_left = -1.00

    if BRes_disp3[0][1] <= -0.50:
        x_right = 0.50
    elif BRes_disp3[0][1] > -0.50 and BRes_disp3[0][1] <= 1:
        x_right = 2.00
    elif BRes_disp3[0][1] > 1:
        x_right = 3.00
    
    dom_xmin = min(BRes_disp3[-1][1]*1.5, x_left) 
    dom_xmax = max(BRes_disp3[0][1]*1.1, x_right) 
    chart_Res = (alt.Chart(BRes_disp3_df).mark_bar().encode(y=alt.Y('Industry:O',
                        sort='-x',axis=alt.Axis(labelAlign='left')),
                        x=alt.X('Performance:Q').scale(domain=[dom_xmin, dom_xmax]),
                                color=clrs_data).properties(height=700)) #labelLimit=300,

   
    st.altair_chart(chart_Res,width="stretch",height="stretch")

    #when only 1 industry selected, show details:
    if len(indus) == 2:            
        indus_details = [(x[0], round(x[2],1), round(x[1],4)) for x in BRes[1][1]]

        indus_details = sorted(indus_details, key=lambda x:x[1], reverse=True)  #ordering for mkt cap
        indus_details2 = []
        #correcting decimals:
        for x in indus_details:
            aa, bb = str(x[1]), str(x[2]*100)
            indus_details2.append((x[0], aa[:aa.index('.')+2]+'B', bb[:bb.index('.')+3]+'%'))
      
        indus_details2_df = pd.DataFrame(indus_details2)

        st.write(f"{BRes[1][0]} (order by market cap):")
        st.dataframe(indus_details2_df, width="content", hide_index=True,
                     column_config={"0":'Ticker',"1":'Market cap',"2":'Performance'})
                
#end of def indus_evaluate*****************************************

def find_sector(tic):
    for gro in fvz.allindus:
        if tic in gro:
            grupo = fvz.indus_names(gro)
            sector_ = grupo[4:grupo.index('-')-1]
            industry_ = grupo[grupo.index('-')+2:]
            
            Ticdata_df = pd.DataFrame([('Sector', sector_),('Industry', industry_)])

            st.dataframe(Ticdata_df, width="content", hide_index=True, height="content",
                         column_config={"0":tic,"1":''})#column_order=None, 
            break
    else:
        st.write(f"no data for {tic}")

def find_tickers(ind):
    gro = fvz.dic_allindus[ind]
    Ticks = []
    for comp in gro:
        try:
            Ticks.append((comp, dat_refs[comp][1]))
        except:
            st.write(f"no data for {comp}")
            continue
    Ticks = sorted(Ticks, key=lambda x:x[1], reverse=True) #order selon mktcap
    Ticks2 = [(x[0], f"{x[1]}B") for x in Ticks]

    Ticks2_df = pd.DataFrame(Ticks2)
    st.dataframe(Ticks2_df, width="content", hide_index=True,column_config={"0":'Ticker',"1":'Market cap'})

#--------------------------------------------------------------------------------------
# program start
st.subheader("S&P500 vs Sectors and Industries")
st.text("""What happens to specific industries when the S&P 500 declines?
This app helps answer questions like that by comparing the performance of the S&P 500 with its sectors or industries. It uses SPY, an ETF that tracks the S&P 500.
Calculations are made between two SPY peaks (marked with red numbers on the chart).

To run a comparison, follow these steps:
1)Select start and end dates
2)Select sector(s) or industry(ies)
3)Press Submit to view the performance list and chart
Note: To see detailed results for each company, select only one industry.

Additional tools:
-Find the sector and industry of a stock (enter a ticker)
-Find largest-cap tickers within a specific industry""", text_alignment="justify")

st.image("Figure_4.png", caption='Evolution of SPY since October 2022')

fe1 = st.selectbox("Select start:", hist_dates02, width=150)
fe2 = st.selectbox("Select end:", hist_dates02, width=150)

fech1 = fe1[fe1.index(')')+2:]  #extracting '(1) '
fech2 = fe2[fe2.index(')')+2:]

sec_calc = st.multiselect("Select sector:", fvz.opts_lis_sectors, width=600)
if st.button("Submit", key="sectors"):
    sector_evaluate(sec_calc, dat_refs, fech1, fech2)

st.divider()
pre_indus_calc = st.multiselect("Select industry:", fvz.opts_industries, width=600)
if '*Select all industries' in pre_indus_calc:
    indus_calc = allindus #['*Select all industries']
else:
    indus_calc = [fvz.dic_allindus[x] for x in pre_indus_calc] #Ex.: [A01,A02]
indus_calc.insert(0,['SPY'])

if st.button("Submit", key="indus"):
    indus_evaluate(indus_calc, dat_refs, fech1, fech2)

st.divider()

st.write("Find the Sector and Industry of a stock:")
tick = (st.text_input("Ticker", width=150)).upper()
if st.button("Find", key="ticker"):
    find_sector(tick)

st.divider()

st.write("Find tickers of an Industry (largest caps):")
indu_t = st.selectbox("Select industry:", fvz.opts_industries[1:], width=450)
if st.button("Find", key="indu_ticks"):
    find_tickers(indu_t)


