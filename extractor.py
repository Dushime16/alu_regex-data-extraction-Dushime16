import re

# Each pattern is saved in a dictionary.
# r"..." means "raw string", so Python does not break the backslashes.

PATTERNS = {
    # user@example.com, firstname.lastname@company.co.uk
    "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b",

    # https://www.example.com, https://subdomain.example.org/page
    "urls": r"https?://[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+(?:/[^\s<>\"']*)?",

    # (123) 456-7890, 123-456-7890, 123.456.7890
    "phones": r"(?:\(\d{3}\)\s?|\b\d{3}[-.])\d{3}[-.]\d{4}\b",

    # 1234 5678 9012 3456, 1234-5678-9012-3456
    "credit_cards": r"\b\d{4}([ -])\d{4}\1\d{4}\1\d{4}\b",

    # 14:30 (24-hour) and 2:30 PM (12-hour)
    "times": r"\b(?:(?:0?[1-9]|1[0-2]):[0-5]\d\s?[AaPp][Mm]|(?:[01]?\d|2[0-3]):[0-5]\d)\b",

    # <p>, <div class="example">, <img src="image.jpg" alt="description">
    "html_tags": r"<[A-Za-z][A-Za-z0-9]*(?:\s+[^<>]*)?/?>",

    # #example, #ThisIsAHashtag
    "hashtags": r"(?<!\w)#[A-Za-z][A-Za-z0-9_]*",

    # $19.99, $1,234.56
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:\.\d{2})?",
}


def extract(data_type, text):
    """Return a list of all matches for one data type."""
    if data_type == "credit_cards":
        # findall with a group returns only the group, so we use finditer
        return [m.group(0) for m in re.finditer(PATTERNS[data_type], text)]
    return re.findall(PATTERNS[data_type], text)


def extract_all(text):
    """Return a dictionary with results for every data type."""
    return {name: extract(name, text) for name in PATTERNS}
