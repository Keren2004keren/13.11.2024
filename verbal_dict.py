# START
text: str = "This chocolate cake is rich, moist, and full of delicious chocolate flavor.\
 To make the cake, you will need chocolate, flour, sugar, eggs, and butter.\
 After baking the chocolate cake, let the cake cool before adding the chocolate frosting."
text_words: list[str] = text.lower().split()
words_count: dict[str, int] = {}
for word in text_words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
most_used: str = max(words_count, key=words_count.get)
print(words_count)
print(f"The word that was most used is '{most_used}', it was used {words_count[most_used]} times.")

only_letter: str = text.replace(",", "").replace(".", "").lower()
letter_count: dict[str, int] = {}
for letter in only_letter:
    if letter.isalpha():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
print(letter_count)
least_used: str = min(letter_count, key=letter_count.get)
print(f"The letter that was least used is '{least_used}', it was used {letter_count[least_used]} time.")

# STOP
