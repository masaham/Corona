# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:47:18 2020

@author: Maria

"""

#cd C:\Users\Maria\OneDrive\Dokumente\Python Scripts\casestudies\corona


#land="Taiwan*"
#land="Switzerland"
def corona(land="Germany"):

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    cor_dat=pd.read_json("https://pomber.github.io/covid19/timeseries.json",orient="index")
    
    #cor_dat[0]["Germany"]
    #cor_dat[1]["Germany"]["recovered"]
    #cor_dat[84]["Germany"]["recovered"]
    
    # cor_dat.index # Liste der Länder
    # cor_dat.index[0:100]
    # cor_dat.index[100:185]
    
    #cd C:\Users\Maria\OneDrive\Dokumente\Python Scripts\casestudies\corona\
    #index=84
    # import datetime
    # today=datetime.datetime.today()
    # begin=datetime.datetime.strptime(cor_dat[0][land]["date"],"%Y-%m-%d")
    # index=int((today-begin)/datetime.timedelta(days=1))-1
    #index=int((today-begin)/datetime.timedelta(days=1))
    index=np.shape(cor_dat)[1]-1
    
    
    
    
    reco=np.array([cor_dat[i][land]["recovered"] for i in range(index)])
    conf=np.array([cor_dat[i][land]["confirmed"] for i in range(index)])
    dead=np.array([cor_dat[i][land]["deaths"] for i in range(index)])
    delta=conf-reco-dead
    Reff=(np.array(conf[index-1])-np.array(conf[index-5]))/(np.array(conf[index-5])-np.array(conf[index-9]))
    plt.figure(figsize=(4,8))
 #   plt.subplots(1, 2, sharex='col')
    plt.subplot(2,1,1)
    plt.title(land+ " " +cor_dat[index][land]["date"]+" R="+str(round(Reff,3)))
    #plt.plot(np.array(delta)*1e-3,"bo-",np.array(reco)*1e-3,"g.",np.array(dead)*1e-3,"m.",np.array(conf)*1e-3,"r.")
    plt.plot(np.array(conf)*1e-3,"r.",label="confirmed: "+str(conf[index-1]))
    plt.plot(np.array(reco)*1e-3,"g.",label="recovered: "+str(reco[index-1]))
    plt.plot(np.array(dead)*1e-3,"m.",label="deaths: "+str(dead[index-1]))
    plt.plot(np.array(delta)*1e-3,"bo-",label="currently infected: "+str(delta[index-1]))
    plt.legend(loc="upper left")
   # plt.xlabel("Elapsed Time (days) since "+ cor_dat[0][land]["date"])
    plt.ylabel("Observations (x1000)")
    #plt.axis([00,85,-5,130])#China
    #plt.axis([20,85,-1,15])#Korea South
    plt.xlim([30,index+1])
    plt.subplot(2,1,2)
    plt.plot(list(range(index-1)),np.array([t - s for s, t in zip(conf, conf[1:])])/1000,"r-",ds="steps",label="confirmed: "+str(np.array(conf[index-1])-np.array(conf[index-2])))
    plt.plot(list(range(index-1)),np.array([t - s for s, t in zip(reco, reco[1:])])/1000,"g-", ds="steps",label="rec: "+str(np.array(reco[index-1])-np.array(reco[index-2])))
    plt.plot(list(range(index-1)),np.array([t - s for s, t in zip(dead, dead[1:])])/1000,"m-",ds="steps", label="deaths: "+str(np.array(dead[index-1])-np.array(dead[index-2])))
    plt.plot(list(range(index-1)),np.array([t - s for s, t in zip(delta, delta[1:])])/1000 ,"b-",ds="steps",label="curr.inf: "+str(np.array(delta[index-1])-np.array(delta[index-2])))
    plt.legend(loc="upper left")

    plt.xlim([30,index+1])
    plt.xlabel("Elapsed Time (days) since "+ cor_dat[0][land]["date"])
    plt.ylabel("Observation-rate (x1000)")
    plt.savefig(cor_dat[index][land]["date"]+land+".png",bbox_inches="tight")
    
    #plt.savefig(cor_dat[index][land]["date"]+"Taiwan"+".png")

    #delta[index-1]
    return conf,reco,dead,delta, index

#plt.scatter(list(range(index)),[t - s for s, t in zip(conf, conf[1:])])







#"https://raw.githubusercontent.com/CSSEGISandData/", 
#  "COVID-19/master/csse_covid_19_data/", "csse_covid_19_time_series/", 
#  "time_series_19-covid-Confirmed.csv", sep = ""


# andere Möglichkeit
# import COVID19Py
# covid19 = COVID19Py.COVID19()
# covid19 = COVID19Py.COVID19(data_source="jhu")
# #location = covid19.getLocationByCountryCode("US", timelines=True)
# location = covid19.getLocationByCountryCode("DE", timelines=True)
# plt.plot(list(location[0]["timelines"]["confirmed"]["timeline"].values()))















