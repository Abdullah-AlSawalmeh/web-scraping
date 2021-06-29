from web_scraper.scraper import *

def test_count():
    assert get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico") == 5

def test_report():
    actual = get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")[:41]
    expected = 'Citation needed for: "The first people to'
    assert actual == expected