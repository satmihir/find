import requests
import re
import gzip
import os
import tarfile


def get_book(book_id):
    url = f"https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
    response = requests.get(url)
    return response.text


def build_phrase_bank(book_text):
    # Extract all 1, 2 and 3 word phrases from the book text in a set
    phrases = set()
    words = book_text.split()
    for i in range(len(words)):
        w = sanitize_word(words[i])
        if w == '':
            continue
        phrases.add(w)

        if i + 1 < len(words):
            w1 = sanitize_word(words[i+1])
            phrases.add(w + " " + w1)

        if i + 2 < len(words):
            w2 = sanitize_word(words[i+2])
            phrases.add(w + " " + w1 + " " + w2)
    phrases = list(phrases)

    with open("phrase_bank.txt", "w") as f:
        for phrase in phrases:
            f.write(phrase + "\n")


def sanitize_word(word):
    # Remove all non-alphabetic characters
    return re.sub(r'[^a-zA-Z0-9]+', '', word.lower())


if __name__ == "__main__":
    # Build phrase bank for the first book
    build_phrase_bank(get_book(1))

    # Download all books and add them to a tarball
    with tarfile.open('books.tar.gz', 'w:gz') as f:
        for i in range(2, 101):
            book_text = get_book(i)
            f.add(book_text, f'book_{i}.txt')
