# Regex Data Extraction

A Python program that uses regular expressions to extract data from text.

## Data types extracted

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- Time (12-hour and 24-hour)
- HTML tags
- Hashtags
- Currency amounts

## Project structure

```
extractor.py        # regex patterns and functions
main.py             # menu program: run on sample file or on your own text
test_extractor.py   # tests for each data type
sample_input.txt    # sample input text
```

## Setup

Requirements: Python 3 and Git. No extra packages are needed.

```
git clone https://github.com/YourUsername/alu_regex-data-extraction-YourUsername.git
cd alu_regex-data-extraction-YourUsername
```

## Usage

Run the program:

```
python3 main.py
```

A menu will appear:

```
--- Regex Data Extractor ---
1. Run on sample_input.txt
2. Type my own text
3. Quit
```

- Type `1` to extract data from `sample_input.txt`.
- Type `2` to type or paste your own text, then see the results.
- Type `3` to quit.

Run the tests:

```
python3 test_extractor.py
```

If all tests pass, you will see `PASS:` for each one.

## Sample output (option 1)

```
=== EMAILS (2 found) ===
   user@example.com
   firstname.lastname@company.co.uk

=== URLS (2 found) ===
   https://www.example.com
   https://subdomain.example.org/page

=== PHONES (3 found) ===
   (123) 456-7890
   123-456-7890
   123.456.7890

=== CREDIT_CARDS (2 found) ===
   1234 5678 9012 3456
   1234-5678-9012-3456

=== TIMES (2 found) ===
   14:30
   2:30 PM

=== HTML_TAGS (3 found) ===
   <p>
   <div class="example">
   <img src="image.jpg" alt="description">

=== HASHTAGS (2 found) ===
   #example
   #ThisIsAHashtag

=== CURRENCY (2 found) ===
   $19.99
   $1,234.56
```

## Example with option 2

Input:

```
Call 123-456-7890 or email me@test.com, price $5.99 #cool
```

The program finds the phone number, the email, the price and the hashtag.

## Edge cases

These invalid inputs are not matched:

- Emails: `hello@`, `user@@example..com`
- Phones: `12-3456-7890`
- Credit cards: `1234 5678-9012 3456` (mixed separators)
- Times: `25:99`

