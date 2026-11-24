from student import SMS


def main() -> None:
    try:
        SMS().start()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting without saving...")


if __name__ == "__main__":
    main()
