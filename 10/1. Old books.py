searching_book = input()
next_book = input()
book_counter = 0
isFound = False

while next_book != "No More Books":
    if next_book == searching_book:
        isFound = True
        break
    book_counter += 1
    next_book = input()
if isFound:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f'The book you search is not here!')
    print(f'You checked {book_counter} books.')