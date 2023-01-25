import sys
sys.path.append("/app")

import unittest
import utils.count_goods_prices as count_goods_prices

class TestGoods(unittest.TestCase):
    def testAddTwoGoodsPrice(self, ):
        testCaseInt = 100
        totalPriceInt = count_goods_prices.countGoodsPrices(goodsPrices=testCaseInt, discount=0)
        self.assertEqual(100, totalPriceInt)

        testInts = [100, 100]
        totalPriceInts = count_goods_prices.countGoodsPrices(testInts, discount=0)
        self.assertEqual(200, totalPriceInts)


if __name__ == "__main__":
    unittest.main()