from hw.alexander_sidorov.lesson06.homework import task_01
from hw.alexander_sidorov.lesson06.homework import task_02
from hw.alexander_sidorov.lesson06.homework import task_03
from hw.alexander_sidorov.lesson06.homework import task_04
from hw.alexander_sidorov.lesson06.homework import task_05
from hw.alexander_sidorov.lesson06.homework import task_06
from hw.alexander_sidorov.lesson06.homework import task_07
from hw.alexander_sidorov.lesson06.homework import task_08
from hw.alexander_sidorov.lesson06.homework import task_09
from hw.alexander_sidorov.lesson06.homework import task_10
from hw.alexander_sidorov.lesson06.homework import task_11
from hw.alexander_sidorov.lesson06.homework import task_12


def test_task_01() -> None:
    got = task_01("")

    assert isinstance(got, dict), f"result {got=!r} MUST be dict"
    assert got, f"empty result {got=!r} is not valid"
    assert len(got) == 1, "only one key is allowed"
    assert ("errors" in got) or ("data" in got), f"unknown key {got.keys()}"

    if "errors" in got:
        errors = got["errors"]
        assert isinstance(errors, list), f"{got['errors']=!r} MUST be a list"
        assert errors, f"{got['errors']=!r} MUST contain at least one error"
        for i, error in enumerate(errors):
            assert isinstance(
                error, str
            ), f"{got['errors'][{i}]=!r} MUST be a str"
        assert errors == sorted(errors), "errors are not sorted"

    assert task_01("") == {"data": True}
    assert task_01("x") == {"data": True}
    assert task_01("xx") == {"data": True}
    assert task_01("xy") == {"data": False}


def test_task_02() -> None:
    assert task_02()


def test_task_03() -> None:
    assert task_03()


def test_task_04() -> None:
    assert task_04()


def test_task_05() -> None:
    assert task_05()


def test_task_06() -> None:
    assert task_06()


def test_task_07() -> None:
    assert task_07()


def test_task_08() -> None:
    assert task_08()


def test_task_09() -> None:
    assert task_09()


def test_task_10() -> None:
    assert task_10()


def test_task_11() -> None:
    assert task_11()


def test_task_12() -> None:
    assert task_12()
