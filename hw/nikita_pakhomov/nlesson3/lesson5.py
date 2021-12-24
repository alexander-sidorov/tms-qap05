def aggression(know: bool) -> str:
    if know:  # noqa: SIM108
        result = "hhh"
    else:
        result = "ggg"
    return result


if __name__ == "__main__":
    aggression(True)
