import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """Fungsi ini digunakan untuk fetch data dari WikiPedia"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    """Mencari nama pada WikiPedia"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Mengembalikan kata kata dari WikiPedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
