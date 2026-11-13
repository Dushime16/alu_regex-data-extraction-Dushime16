from extractor import extract


def test_email():
    assert extract("emails", "a user@example.com b") == ["user@example.com"]
    assert extract("emails", "hello@") == []          # edge case


def test_url():
    assert extract("urls", "go https://www.example.com now") == ["https://www.example.com"]


def test_phone():
    text = "(123) 456-7890 123-456-7890 123.456.7890"
    assert len(extract("phones", text)) == 3
    assert extract("phones", "12-3456-7890") == []    # edge case


def test_credit_card():
    assert len(extract("credit_cards", "1234 5678 9012 3456")) == 1
    assert len(extract("credit_cards", "1234-5678-9012-3456")) == 1
    assert extract("credit_cards", "1234 5678-9012 3456") == []  # mixed separators


def test_time():
    assert extract("times", "at 14:30") == ["14:30"]
    assert extract("times", "at 2:30 PM") == ["2:30 PM"]
    assert extract("times", "25:99") == []            # edge case


def test_html():
    assert extract("html_tags", '<img src="image.jpg" alt="description">') == \
        ['<img src="image.jpg" alt="description">']


def test_hashtag():
    assert extract("hashtags", "#example #ThisIsAHashtag") == ["#example", "#ThisIsAHashtag"]


def test_currency():
    assert extract("currency", "$19.99 and $1,234.56") == ["$19.99", "$1,234.56"]


if __name__ == "__main__":
    for name, func in list(globals().items()):
        if name.startswith("test_"):
            func()
            print("PASS:", name)
