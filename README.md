# FIND

FIND is a Go library designed for highly efficient detection of phrases from a large static corpus within any given text sample. Leveraging advanced algorithms like rolling hashes and minimal perfect hashing, FIND provides ultra-fast lookups, making it suitable for performance-critical applications.

FIND's design is optimized specifically for static phrase sets, ensuring maximum speed and minimal memory overhead during phrase detection.


## Example Use Cases

1. **Content Moderation:** Rapid detection and removal of offensive or inappropriate language from LLM-generated, user-generated, or randomly generated text streams.
2. **Spam Detection and Filtering:** Quickly identifying known spam phrases or malicious patterns in real-time messaging applications, forums, or comment sections.
3. **Real-time Document Tagging:** Quickly identifying and categorizing documents based on the presence of key phrases.

I could go on but you get the idea. If you want to process texts to quickly detect presence of certain words (you fully own this dataset) such that these words are known in advance, this is the right library for you.
