class SliceData:
    def sliceFirstTenData(dict):
        liste = []
        first2pairs = {k: dict.to_dict(orient='index')[k] for k in list(dict.to_dict(orient='index'))[:10]}
        # print(first2pairs)
        for i in range(10):
            liste.append(first2pairs[i])
        return str(liste)
