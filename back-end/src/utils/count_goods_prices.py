from typing import List, Union
from functools import reduce

def countGoodsPrices(goodsPrices: Union[int, List[int]], discount: Union[int, float] = 0) -> int:
    goodsPricesDiscount = 1 - discount 
    if type(goodsPrices) == int:
        return int(goodsPrices * goodsPricesDiscount)
    else:
        totalPriceOrigin = reduce(lambda acc, nextV: acc + nextV, goodsPrices, 0)
        totalPriceDiscounted = totalPriceOrigin * goodsPricesDiscount
        return int(totalPriceDiscounted)
