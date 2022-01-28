from datetime import date

from hw.maria_saganovich.final import DupCounter05
from hw.maria_saganovich.final import HttpQuery03
from hw.maria_saganovich.final import Multiplier04
from hw.maria_saganovich.final import Palindrome01
from hw.maria_saganovich.final import User02


def test_final() -> None:
    palindrome1 = Palindrome01("xx")
    palindrome2 = Palindrome01("xy x")
    palindrome3 = Palindrome01(123)
    assert palindrome1.__bool__()
    assert not palindrome2.__bool__()
    assert palindrome3.__bool__() == {"errors": ["Should be string"]}

    birthday = date(2020, 1, 23)
    user_info = User02(birthday)
    assert user_info.age == 2
    user_info2 = User02("2001-01-02")
    assert user_info2.age == {"errors": ["should be date"]}

    query = HttpQuery03("x=1&y=2&y=3")
    assert query["x"] == "1"
    assert query["y"] == ["2", "3"]
    assert query["z"] is None
    query2 = HttpQuery03(123)
    assert query2["x"] == {"errors": ["arg should be str"]}

    mult = Multiplier04()
    mult.add(2).add(3).add(4)
    assert mult.get_result() == 24

    duplicate = [1, 1, 1, 1, 2, 2, 3]
    data = DupCounter05(duplicate)
    assert data.get_dups() == {1: 4, 2: 2}
    data2 = DupCounter05(123)
    assert data2.get_dups() == {"errors": ["No Collections"]}