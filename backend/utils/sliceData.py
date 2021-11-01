import json
from flask.json import jsonify
from bson import json_util


class SliceData:
    def sliceFirstTenData(dict):
        liste = []
        first2pairs = {k: dict.to_dict(orient='index')[k] for k in list(dict.to_dict(orient='index'))[:10]}
        # print(first2pairs)
        print(first2pairs[0])
        for i in range(10):
            liste.append(first2pairs[i])
        print(liste)
        a = str(liste).replace("\'", "\"")
        return str(liste)
