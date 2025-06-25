# Louis Deschamps TDA G2 - 27/11/2024
# SAE105

import requests
import json
import time

# pour la carte
import folium

# pour les graph
import matplotlib.pyplot as plt
from datetime import datetime

def parsing(file):
    print("lecture de "+file, end="")
    log = []
    f = open(file,"r")
    for x in f:
        ip = x.split(" ")[0]
        time = x.split("[")[1].split("]")[0]
        method = x.split('"')[1].split(" ")[0]
        if method == "-":
            page=""
            code=x.split(" ")[6]
            size=x.split(" ")[7] # en octée
            ua=""
        else:
            page = x.split(" ")[6]
            code = x.split(" ")[8]
            size = x.split(" ")[9] # en octée
            ua = x.split('"')[5]
        log.append([ip,time,method,page,code,size,ua])
    f.close()
    print("  OK")
    return log

def getIP_APIrequest(query):
    url = 'http://ip-api.com/batch'
    x = requests.post(url,json.dumps(query))
    return json.loads(x.text)
def getIP_infos(IPlist):
    print("analyse des IP  ",end="")
    IPdb = {}
    for i in range(len(IPlist)):
        if IPlist[i] not in IPdb:
            IPdb[IPlist[i]]={}
    query=[]
    for ip in IPdb:
        query.append(ip)
        if len(query) > 99:
            result = getIP_APIrequest(query)
            for value in result:
                if value["status"] == "success":
                    IPdb[value["query"]]=value
            time.sleep(4)
            query=[]
    result = getIP_APIrequest(query)
    for value in result:
        if value["status"] == "success":
            IPdb[value["query"]]=value
    print("OK")
    return IPdb


def createmap(IPdb,filename):
    print("nombre de marqueur a posée : "+ str(len(IPdb)))
    print("creation de la carte", end="")
    m = folium.Map()
    for ip in IPdb:
        if len(IPdb[ip]) > 0 :
            folium.Marker(
                location=[IPdb[ip]["lat"], IPdb[ip]["lon"]],
                tooltip=ip,
                icon=folium.Icon(),
            ).add_to(m)
    m.save(filename)
    print("   OK")

def plotrequest(data,filename):
    print("creation du graph", end="")
    timerequest = {}
    for log in data:
        hour = datetime.strptime(log[1], "%d/%b/%Y:%H:%M:%S %z").replace(minute=0, second=0, microsecond=0)
        if hour not in timerequest:
            timerequest[hour]=0
        timerequest[hour]+=1
    x = sorted(timerequest.keys())
    y = [timerequest[hour] for hour in x]
    plt.figure(figsize=(19.20,10.80))
    plt.plot(x,y)
    plt.xlabel('Date')
    plt.ylabel('Nombre de requêtes')
    plt.title('Nombre de requêtes par heure')
    plt.grid(True)
    plt.savefig(filename)
    print("   OK")

def plotOS(data,filename):
    print("creation du graph", end="")
    OS={
        "windows":0,
        "linux":0,
        "mac":0,
        "bot":0,
        "autre":0
    }
    for a in data:
        if "Windows" in a[6]:
            OS["windows"]+=1
        elif "X11" in a[6] or "Linux" in a[6] or "Android" in a[6] :
            OS["linux"]+=1
        elif "Mac OS" in a[6]:
            OS["mac"]+=1
        elif "http" in a[6] or "Bot" in a[6] or "bot" in a[6] or "@" in a[6] or ".com" in a[6] or "ExtraireLiensNomDomaine" in a[6]:
            OS["bot"]+=1
        elif a[6] != "-" and a[6] != "" : 
            OS["autre"]+=1
    plt.figure()
    for names in OS:
        plt.bar(names, OS[names])
    plt.xlabel('OS')
    plt.ylabel('Nombre de requêtes')
    plt.title('Nombre de requêtes par OS')
    plt.grid(True)
    plt.savefig(filename)
    print("   OK")

def plotCode(data,filename):
    print("creation du graph", end="")
    code={}
    for a in data:
        if a[4] != '"-"' and a[4] != "0":
            if a[4] not in code:
                code[a[4]]=0
            code[a[4]]+=1
    plt.figure()
    for names in code:
        plt.bar(names, code[names])
    plt.xlabel('Code HTTP')
    plt.ylabel('Nombre de requêtes')
    plt.title('Nombre de requêtes par code HTTP')
    plt.grid(True)
    plt.savefig(filename)
    print("   OK")

# extrait data chaque ligne de log sous la forme [[ip,time,method,page,code,size,ua],etc...]
# exemple : data[104][6] = récupère le user agent (UA) de la ligne 104 du fichier logs
data = parsing("controltower_access.log")

# extrait data dans IPdb tous les IPs pour créer un dictionnaire sous la forme {"ip" : {réponse API}, etc...}
# l'API répond sous la forme d'un JSON (qui est converti en dictionnaire). exemple : {"status": "success","country": "France","countryCode": "FR","region": "IDF","regionName": "Île-de-France","city": "Paris","zip": "75000","lat": 48.8566,"lon": 2.35222,"timezone": "Europe/Paris","isp": "BOUYGUES Telecom","org": "","as": "AS5410 Bouygues Telecom SA","query": "80.215.104.47"}
# exemple : IPdb["54.36.148.188"]["country"] = "France"
IPdb = getIP_infos([x[0] for x in data])

# crée une carte de tous les IPs, et l'enregistre dans le fichier "index.html"
createmap(IPdb,"out/maps.html")

# crée un graphique du nombre de requêtes pour chaque heure, et l'enregistre dans le fichier "request.png"
plotrequest(data,"out/request.png")

# crée un graphique des OS utilisés, et l'enregistre dans le fichier "os.png"
plotOS(data,"out/os.png")

# crée un graphique des codes HTTP utilisés, et l'enregistre dans le fichier "httpCode.png"
plotCode(data,"out/httpCode.png")


