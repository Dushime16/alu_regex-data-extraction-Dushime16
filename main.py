from extractor import extract_all


def main():
    # Read the sample text from the file
    with open("sample_input.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Find all the data
    results = extract_all(text)

    # Show the results
    for name, matches in results.items():
        print(f"\n=== {name.upper()} ({len(matches)} found) ===")
        for item in matches:
            print("  ", item)


if __name__ == "__main__":
    main()
