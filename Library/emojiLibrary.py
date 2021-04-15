import emoji

print(emoji.emojize('Python is :thumbs_up:'))


import emoji
print(emoji.emojize('Python is :thumbs_up:'))
# Python is 👍

print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
# Python is 👍

print(emoji.demojize('Python is 👍'))
# Python is :thumbs_up:

print(emoji.emojize("Python is fun :red_heart:"))
# Python is fun ❤

print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
# Python is fun ❤️ #red heart, not black heart