ddd={
            "white forest1 kg": [10,400],
            "black forest1 kg": [10,350],
            "pinp cake250 gm":  [10,250],
            "butter scotch250 gm  ":[10,250],
            "chocolate250 gm ": [10,200],
            "antique4 lts":  [10,862],
            "antique1 lts":    [20,223],
            "shyne20 lts":      [10,2411],
            "shyne10 lts":      [10,1273],
            "shyne4 lts":     [10,546],
            "shyne1 lts":      [25,144],
            "classic20 lts":    [15,1857],
            "classic10 lts":    [10,979],
            "classic4 lts":    [12,424],
            "classic1 lts":    [14,114]}
from KEEpydb import KEEpydb as k
a=k.query('bakeryshop','rajat','rajat@143')
d='a'
dd=2
for i in ddd.keys():
    a.update(d,i)
    d='a'+str(dd+1)
