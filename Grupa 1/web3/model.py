podaci = {
    "1":{
        "ime":"Arya Stark","popularnost":4,"slika":"https://static.wikia.nocookie.net/gameofthrones/images/b/be/AryaShipIronThrone.PNG"
    },
    "2":{
        "ime":"Khal Drogo","popularnost":3,"slika":"https://static1.moviewebimages.com/wordpress/wp-content/uploads/2022/11/khal-drogo-game-of-thrones.jpg?q=50&fit=contain&w=1140&h=&dpr=1.5"
    },
    "5":{
        "ime":"Hodor","popularnost":5,"slika":"https://static.wikia.nocookie.net/gameofthrones/images/1/18/Season_6_hodor_main.jpg"
    },
    "13":{
        "ime":"Tyrion Lannister","popularnost":5,"slika":"https://static.wikia.nocookie.net/gameofthrones/images/9/95/HandoftheKingTyrionLannister.PNG"
    }
}

def svipodaci():
    return podaci

def podatak(pid):
    return podaci[pid]

def dodaj(ime,popularnost,slika):
    najveci = 0
    for k in podaci:
        if int(k) > najveci:
            najveci = int(k)
    podaci[najveci+1] = {"ime":ime,"popularnost":popularnost,"slika":slika}
        