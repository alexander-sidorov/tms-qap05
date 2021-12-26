def aggression(know: bool) -> str:
    if know:
        result = "оно и видно!"
    else:
        result = "а могли бы и знать!"

    return result


if __name__ == "__main__":
    aggression(True)
