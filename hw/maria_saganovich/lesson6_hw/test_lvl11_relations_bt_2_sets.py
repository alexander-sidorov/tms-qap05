from hw.maria_saganovich.lesson6_hw.lvl11_relations_bt_2_sets import (
    func11_relation_bt_2_sets,
)


def test_func11_relation_bt_2_sets() -> None:
    assert func11_relation_bt_2_sets({1, 2}, {1, 3}) == {
        "data": {
            "a&b": {1},
            "a|b": {1, 2, 3},
            "a-b": {2},
            "b-a": {3},
            "|a-b|": {2, 3},
            "a in b": False,
            "b in a": False,
        }
    }
    assert func11_relation_bt_2_sets({1, 2}, {1, 2, 3}) == {
        "data": {
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": set(),
            "b-a": {3},
            "|a-b|": {3},
            "a in b": True,
            "b in a": False,
        }
    }
    assert func11_relation_bt_2_sets({1, 3}, {1, 3}) == {
        "data": {
            "a&b": {1, 3},
            "a|b": {1, 3},
            "a-b": set(),
            "b-a": set(),
            "|a-b|": set(),
            "a in b": True,
            "b in a": True,
        }
    }
    assert func11_relation_bt_2_sets({1}, {""}) == {
        "data": {
            "a&b": set(),
            "a|b": {"", 1},
            "a-b": {1},
            "b-a": {""},
            "|a-b|": {"", 1},
            "a in b": False,
            "b in a": False,
        }
    }
    assert func11_relation_bt_2_sets([], {""}) == {
        "errors": ["arg should be set"]
    }
    assert func11_relation_bt_2_sets({""}, []) == {
        "errors": ["arg should be set"]
    }
