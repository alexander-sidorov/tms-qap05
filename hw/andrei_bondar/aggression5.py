def aggression(know: bool) -> str:
    if know:
        result = "оно и видно"
    else:
        result = "а мог бы и знать"

    return result

1
if __name__ == "__main__":
    aggression(True)
