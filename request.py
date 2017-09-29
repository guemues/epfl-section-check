import requests

url = "https://isa.epfl.ch/imoniteur_ISAP/%21PORTAL14S.portalCell"

querystring = {"ww_k_cell":"1809191822","zz_n_xmlBufferKey":"107242052","ww_n_cellkey":"9845106311","ww_n_ctrlKey":"145587473"}

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "tr-TR,tr;q=0.8,en-US;q=0.6,en;q=0.4",
    'cookie': "LANGUE_LOGIN=en; ISA-CNXKEY=446CAEEFF4C8EAF146139D883C7B4A77; __utma=33657086.795605702.1478022787.1491756107.1495825137.44; __utmz=33657086.1495825137.44.16.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); petitpois=dismiss; _ga=GA1.2.795605702.1478022787; _gid=GA1.2.794847808.1505644860",
    'cache-control': "no-cache",
    'postman-token': "46d94a55-81bc-ee4f-5bf7-31c4de143a8a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)