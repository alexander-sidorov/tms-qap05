from hw.alexander_sidorov.lesson05.homework import hack


def test_hack() -> None:
    cipher = "cbDDC NCyDm"
    key = "inhmbGOWdZEDMpCXvyYoVRNBFSkIrwAtscuzflTgaLqUHxKjPJQe"

    response = hack(cipher, key)

    assert response == "Hello world"
