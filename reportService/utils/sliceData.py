import json 

class SliceData:
    def sliceFirstTenData(deger):
        liste = []
        liste.append(deger[6])
        liste.append(deger[7])
        liste.append(deger[8])
        liste.append(deger[9])
        liste.append(deger[10])
        liste.append(deger[11])
        liste.append(deger[12])
        liste.append(deger[13])
        liste.append(deger[14])
        liste.append(deger[15])

        sonuc = json.dumps(liste)
        # print(sonuc)
        return liste
    