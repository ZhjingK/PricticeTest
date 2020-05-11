import pytest
import yaml

from python.calculator import Calc

import sys
sys.path.append("..")

"""
用例设计：
数值型(大数、小数、正数、负数)
字符型

考虑使用pytest.mark.parametrize()进行参数化
考虑使用pytest.mark.xfail()进行预期失败
"""


class TestCalc:
    def setup(self):
        self.cal = Calc()

    # @pytest.mark.parametrize("a,b,result", [
    #     (-12, -10, -22),
    #     (-0.1, -0.4, -0.5),
    #     (-12, 0.3, -11.7),
    #     (-0.4, 2, 1.6),
    #     (12, 90, 102),
    #     (+12, 0, 12),
    #     (-0.1, 0, -0.1),
    #     ({1, 2}, 9, "no result"),
    #     ([1, 2], 0, "no result"),
    #     ("a", "b", "a+b")])
    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open("/Users/zhangjing1/Desktop/practice/data/add.yaml")))
    def test_add(self, a, b, result):
        print(a, b, result)
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(result, (int, float)):
            call = self.cal.add(a, b)
            assert call == result
        else:
            with pytest.raises(TypeError):
                self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,result", yaml.safe_load(open('/Users/zhangjing1/Desktop/practice/data/div.yaml')))
    def test_div(self, a, b, result):
        print(a, b, result)
        if b == 0:
            pytest.raises(ZeroDivisionError)
            self.cal.div(a, b)
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(result, (int, float)):
            call = self.cal.div(a, b)
            assert call == result
        else:
            pytest.raises(TypeError)
            self.cal.div(a, b)


if __name__ == '__main__':
    pytest.main()