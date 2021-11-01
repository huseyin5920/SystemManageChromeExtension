class SliceData:
    def sliceFirstTenData(dict):
        first2pairs = {k: dict.to_dict(orient='index')[k] for k in list(dict.to_dict(orient='index'))[:10]}
        # print(first2pairs)
        print(first2pairs[0])
        return first2pairs
