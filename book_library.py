print("****************Welcome to Book Management system****************")
print()
book_list = []

book_num = int(input("Enter how many books you want to add to the library: "))

for _ in range(book_num):
    title = input("Enter book name:")
    author = input('Enter author:')
    genre = input('Enter genre:')
    copies = input('Enter available copies:')
    print("*"*20)

    book_dict = {"Title": title, "Author": author,
                 "Genre": genre, "Copies": copies}
    book_list.append(book_dict)

print('Book Information:')
for idx, book_dict in enumerate(book_list, start=1):
    print(f"Book: {book_dict['Title']}")
    print(f"Author: {book_dict['Author']}")
    print(f"Genre: {book_dict['Genre']}")
    print(f"Copies: {book_dict['Copies']}")
    print("*"*20)

search_book = input("Serch book by Title:")

found = False

for book_dict in book_list:
    if book_dict['Title'].lower() == search_book.lower():
        print(f"Book: {book_dict['Title']}")
        print(f"Author: {book_dict['Author']}")
        print(f"Genre: {book_dict['Genre']}")
        print(f"Copies: {book_dict['Copies']}")
        found = True
        break
if not found:
    print('No matches!')
