"""
NEW WAY: Unicode Grapheme Clusters in Python 3.15

A visible character can contain multiple Unicode code points.
iter_graphemes() helps us process visible characters correctly.
"""

import unicodedata


# Example 1: A letter with a combining accent.
text = "e\u0301"

print("Text:", text)

# len() counts Unicode code points, not visible characters.
print("Code points:", len(text))

# Python 3.15 groups code points into grapheme clusters.
characters = list(unicodedata.iter_graphemes(text))

print("Visible characters:", len(characters))
print("Graphemes:", characters)


# Example 2: A family emoji.
emoji = "👨‍👩‍👧‍👦"

print("\nEmoji:", emoji)
print("Code points:", len(emoji))

# The family emoji is treated as one grapheme cluster.
emoji_characters = list(unicodedata.iter_graphemes(emoji))

print("Visible characters:", len(emoji_characters))
print("Graphemes:", emoji_characters)