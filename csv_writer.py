import os
from book import Book
import csv

def str_or_empty(str):
	if str is None:
		return ''
	else:
		return str

def format_book(book):
	return [book.id, str_or_empty(book.name), str_or_empty(book.ISBN), book.rating, book.date]

# Write books content to csv file
class CsvWriter():
	def save(this, books, file_name):
		with open(file_name, 'w', encoding="utf-8") as file:
			writer = csv.writer(file, delimiter=';', lineterminator='\n')
			writer.writerow(['ID', 'Title', 'ISBN', 'My Rating', 'Date Added'])
			for book in books:
				writer.writerow(format_book(book))
