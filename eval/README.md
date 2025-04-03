# Evaluation

This directory contains the data to evaluate FIND. For evaluation as well as testing, we use the first hundred books from [Project Gutenberg](https://www.gutenberg.org/). We use the first book to extract all 1, 2 and 3 word phrases (~32000 total) and we look them up in books 2 through 100. All books are run serially after loading everything in memory. The total time to find phrases in all books is the metric we use to evaluate various approaches.

## Data Storage

To make the evaluation process offline, we store all Project Gutenberg books locally in a tarball called `books.tar.gz`. The phrase bank to check against is stored in `phrase_bank.txt`.