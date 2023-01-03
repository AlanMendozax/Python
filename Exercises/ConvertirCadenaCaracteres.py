# Import the regular expression module
import re

# Initialize the string to be modified
t = "La 1 - en + la () de su LYA1 con el LYA1 final 3 5 puntos MO"

# Replacing the pattern:
# The r before a string indicates that the string is a raw string. A raw string is a string literal
# that is not interpreted by the Python interpreter, so all characters in the string are taken literally.
# We use \b only if it is a complete word (surrounded by word boundaries). Characters are
# word boundary assertions.
# "\s*\" is a regular expression pattern that matches zero or more white space characters.
# The \s pattern matches any white space character (such as a space, tab, or newline), and
# the * character indicates that the preceding pattern should be matched zero or more times.
# re.sub() is a function in the re (regular expression) module that performs a search-and-replace
#  operation on a string. It takes three arguments:
# pattern: This is the regular expression pattern to search for.
# replacement: This is the string to use as a replacement for the pattern.
# string: This is the string to search and replace in.
# re.sub() returns a new string with all occurrences of the pattern replaced by the replacement string.

# For example, consider the following code:
nc = re.sub(r"\b1\b", "primera", t)
nc = re.sub(r"-", "persona", nc)
nc = re.sub(r"\+", "mandarme", nc)
nc = re.sub(r"\(\s*\)", "foto", nc)
nc = re.sub(r"LYA1", "programa", nc)
nc = re.sub(r"\b3\b", "obtiene", nc)
nc = re.sub(r"\bMO\b", "extra", nc)

# Print the modified string
print(nc)