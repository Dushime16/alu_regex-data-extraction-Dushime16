from extractor import extract_all


def show_results(text):
    """Find the data in the text and print it."""
    results = extract_all(text)

    for name, matches in results.items():
        print(f"\n=== {name.upper()} ({len(matches)} found) ===")
        for item in matches:
            print("  ", item)


def main():
    while True:
        print("\n--- Regex Data Extractor ---")
        print("1. Run on sample_input.txt")
        print("2. Type my own text")
        print("3. Quit")

        choice = input("Choose 1, 2 or 3: ")

        if choice == "1":
            with open("sample_input.txt", "r", encoding="utf-8") as file:
                text = file.read()
            show_results(text)

        elif choice == "2":
            text = input("Type or paste your text: ")
            show_results(text)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Wrong choice. Please type 1, 2 or 3.")


if __name__ == "__main__":
    main()
