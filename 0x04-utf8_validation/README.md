# 0x04. UTF-8 Validation

UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding standard that is widely used for representing and handling text in various programming languages and systems. It is part of the Unicode standard and is designed to be backward-compatible with ASCII (American Standard Code for Information Interchange).

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: `def validUTF8(data)`
- Return: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
