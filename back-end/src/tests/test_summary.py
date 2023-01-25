import sys
sys.path.append("/app")

import unittest
import utils.count_goods_prices as count_goods_prices

class TestGoods(unittest.TestCase):
    def setUp(self) -> None:
        self.discount = 0
        return super().setUp()

    def testAddTwoGoodsPrices(self, ):
        testCaseInt = 100
        totalPriceInt = count_goods_prices.countGoodsPrices(goodsPrices=testCaseInt, discount=self.discount)
        self.assertEqual(100, totalPriceInt)

        testInts = [100, 100]
        totalPriceInts = count_goods_prices.countGoodsPrices(testInts, discount=self.discount)
        self.assertEqual(200, totalPriceInts)

    def testAddTwoGoodsPricesWithDiscount(self, ):
        self.discount = 0.5

        testCaseInt = 100
        totalPriceInt = count_goods_prices.countGoodsPrices(goodsPrices=testCaseInt, discount=self.discount)
        self.assertEqual(50, totalPriceInt)

        testInts = [100, 100]
        totalPriceInts = count_goods_prices.countGoodsPrices(testInts, discount=self.discount)
        self.assertEqual(100, totalPriceInts)


if __name__ == "__main__":
    unittest.main()