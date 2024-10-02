# Python code equivalent of the C++ code

class Library:
	def __init__(self, book_name, author, pages, price):
		self.book_name = book_name
		self.author = author
		self.pages = pages
		self.price = price

	def __str__(self):
		return f"{self.book_name}\t {self.author}\t {self.pages}\t {self.price}"


# Driver Code
if __name__ == "__main__":
	# Create an array of Library objects
	lib = []

	# Keep the track of the number of
	# of books available in the library
	count = 0

	# Iterate the loop
	while True:
		print("\n\n********######WELCOME TO E-LIBRARY #####********\n")
		print("1. Add book information\n2. Display book information\n", 
			"3. List all books of given author\n4. List the count of books in the library\n5. Exit\n")

		# Enter the book details
		input_choice = input("Enter one of the above: ")

		# Process the input
		if input_choice == '1':
			book_name = input("Enter book name = ")
			author = input("Enter author name = ")
			pages = int(input("Enter pages = "))
			price = float(input("Enter price = "))
			lib.append(Library(book_name, author, pages, price))
			count += 1
		elif input_choice == '2':
			print("you have entered the following information")
			for book in lib:
				print(book)
		elif input_choice == '3':
			ar_nm = input("Enter author name : ")
			for book in lib:
				if book.author == ar_nm:
					print(book)
		elif input_choice == '4':
			print(f"\nNo of books in library : {count}\n")
		elif input_choice == '5':
			exit(0)
