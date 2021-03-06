"""
@brief      test log(time=2s)
"""


import sys, os, unittest


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.pyensae.finance.astock import StockPrices


class TestStockGraph2 (unittest.TestCase):

    def test_graph2(self) :
        """
        This test is failing with Python 3.4 if many pictures are drawn.
        """
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")

        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache2")
        stock = StockPrices ("BNP.PA", folder = cache)
        stock2 = StockPrices ("CA.PA", folder = cache)

        fig, ax, plt = stock.plot(figsize=(16,8))
        fig, ax, plt = stock2.plot(existing=(fig,ax))
        img = os.path.abspath(os.path.join(os.path.split(__file__)[0],"temp_image2.png"))
        if os.path.exists(img): os.remove(img)
        fig.savefig(img)
        assert os.path.exists(img)


if __name__ == "__main__"  :
    unittest.main ()