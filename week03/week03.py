import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)

tlist=data["result"]["results"]
with open ("data.csv","w",encoding="utf-16") as file:
    for i in tlist:
        x = i["file"]
        y= x.split("https://")
        lines=[i["stitle"],",",i["address"][5:8],",",i["longitude"],",",i["latitude"],",",("https://"+y[1]),"\t","\n"]
        file.writelines(lines)



       
     
        
       

    
    

                
