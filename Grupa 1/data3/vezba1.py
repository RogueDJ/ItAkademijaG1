SNAGA=1
KONDICIJA=2
RAZGIBAVANJE=3
treninzi = [
    ["Burpi",30,KONDICIJA],
    ["Skelkovi",40,SNAGA],
    ["Cucnjevi",20,SNAGA],
    ["Trbusnjaci",60,KONDICIJA],
    ["Istezanje",30,RAZGIBAVANJE]
]

ukupno_snaga=0
for naziv,vreme,tip in treninzi:
    ukupno_snaga+=vreme if tip == SNAGA else 0

print(ukupno_snaga)