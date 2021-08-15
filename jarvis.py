import pandas as pd
import requests

url = "https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837"
res = []
for x in range(1, 5):
    querystring = {
        "isProductNeeded": "true",
        "orderBy": ["default", "default", "default"],
        "pageSize": "100",
        "responseFormat": "json",
        "isChanelCategory": "false",
        "currency": "USD",
        "pageView": "image",
        "viewTaskName": "CategoryDisplayView",
        "beginIndex": "0",
        "categoryId": "3074457345626651837",
        "catalogId": "20602",
        "langId": "-1",
        "currentPage": f"{x}",
        "storeId": "10152",
        "top": "Y",
    }
    headers = {
        "cookie": "bm_sv=2B9D9734DEE6A960841D70819F16C15C~3ugTB01WsVMCx4yE3rwulZrdivjV42a%2Bu7H8vw1jWo0P%2BCX3J1w1MIreSa%2BwLPUP8LGsMqQgt5o5gK4RMQ0WXHUUh5%2BP2LI8xNMCFsQhaayFWR4Mz28We6yPJeAhih4a3T%2BrDCoFc72sXvWDPOibxbE2aCcuaFZNrP0z9mUTYyw%3D; TS011f624f=015966d292fa160a353c94a8b1521ba49ef109d172ac9babf9e638461c9af985a7db453dcc16fbe84e19e83755c3efd23b4b46455019a17308a2ee6a689f2f9b3d4d328258",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "X-NewRelic-ID": "VQ4GVFNbChABVlRTBwcPUF0=",
        "Connection": "keep-alive",
        "Referer": "https://www.sunglasshut.com/us/mens-sunglasses",
        "Cookie": "aka-cc=US; aka-ct=ORTING; aka-zp=98360; ak_bmsc=6B2C1F4E5C41C2F5AFE5215E35D477D3~000000000000000000000000000000~YAAQBgNAF1ML90R7AQAAepivRgw8TprGMBIkeU7gPjZ0KWQgdKdKcgUqzDG0dhLKdAOMde5NjEPoQzOF3di2UGbQQguupcf4SID5H1B0c7E5Gfw41oSbP3x9EhxZ0NRqvSFi2k4MsuCge6+AOwrw3Kg4MFxtDwPHh7QJxA6nccWvvJib1Cc1MwidF2XikeVdTUhdLsr7D/MJA7DUMo0YdgE7df7V7iM9C/+tFPcYaH8Pn43sHeGz/749z47S7k7F2OLkuQdjweidxEEvtFjUOZtdf8rmm9bUkcvJRc257FTtk5K3NZgpmq+Tjr3i5L8okti2ho/uYF1OoowQ637pHptKQ817tzz0oLknaPPGr+gzJEzwCd+bnANQcoPtxzC/IhNwfeKpRjBmHFjAQKgg/SJVte1SKV1bXL88pmCo6a888JxSgJ9I6pv0rUoTPB1Un78oJ71XjS6Cs+5rHL/GRf63eTrHB37Z55MZ2tFkktHwvK/lpT6NPUb7QN7u2A==; SGPF=36FvmLfiso0-XHXhyfUWpOo-Z8IVPGCYesJj90bP055A4epcE7ipj2w; forterToken=5320aeff6faa4b5cbe7aff1a5c80f6f4_1628978649049__UDF43_6; dtCookie=v_4_srv_5_sn_CI7T711CBGGBVLQAQF5PT8PKT2RV718Q_app-3Ab359c07662f0b428_0_ol_0_perc_100000_mul_1; rxVisitor=1628978516727K8JCTP92VLHAN8NVLLNL3FR7D5LVQPTF; dtPC=5$578534868_494h1p5$578648897_736h1vMUWOLJCAAAMKVAVCQAHGFWMHGSKPKFAG-0e1; rxvt=1628980318613|1628978516728; dtSa=-; dtLatC=39; sgh-desktop-facet-state-plp=categoryid:undefined|gender:true|brands:partial|polarized:true|price:true|frame-shape:partial|color:true|face-shape:false|fit:false|materials:false|lens-treatment:false; sgh-desktop-facet-state-search=; mt.v=2.377053422.1628978517476; ftr_ncd=6; __wid=211863964; JSESSIONID=0000JKNHaIcDZeHOEYsbKm6pa5V:1c7qtqjbr; TS011f624f=015966d292cd327706a05be969034a208d7c0a627585f264e59b7b590afcce2c26a23cf8459742909cadf5a0d6ce5f73d5bc92794640de24e404de204beba693faa4f634b3; bm_sv=2B9D9734DEE6A960841D70819F16C15C~3ugTB01WsVMCx4yE3rwulZrdivjV42a+u7H8vw1jWo0P+CX3J1w1MIreSa+wLPUP8LGsMqQgt5o5gK4RMQ0WXHUUh5+P2LI8xNMCFsQhaazsZHro+jSnJ4znptjSMrKTu0/GJErNaMjwL5IIuxuZR8JmcARgZP4nlH5npqPtru4=; utag_main=v_id:017b46af9675000741d4d3f3958c00052001c00f019b8$_sn:1$_se:9$_ss:0$_st:1628980449136$ses_id:1628978517621%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:sunglasshut.com$dc_visit:1$dc_event:1%3Bexp-session; tealium_data_session_timeStamp=1628978517632; userToken=undefined; AMCV_125138B3527845350A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C18854%7CMCMID%7C70969032584924622153885104860349826509%7CMCAAMLH-1629583318%7C9%7CMCAAMB-1629583318%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1628985718s%7CNONE%7CMCSYNCSOP%7C411-18861%7CMCAID%7CNONE%7CvVersion%7C3.3.0; _cs_mk=0.29679904897047915_1628978517733; AMCVS_125138B3527845350A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C70969032584924622153885104860349826509; s_cc=true; rxVisitor=1628978516727K8JCTP92VLHAN8NVLLNL3FR7D5LVQPTF; dtSa=-; CONSENTMGR=consent:true%7Cts:1628978647960",
    }
    r = requests.request("GET", url, headers=headers, params=querystring)
    data = r.json()
    for p in data["plpView"]["products"]["products"]["product"]:
        res.append(p)
df = pd.json_normalize(res)
df.to_csv("firstresults.csv")
