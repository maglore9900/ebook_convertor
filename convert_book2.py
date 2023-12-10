import os, fnmatch, sys, subprocess

a = []
if len(sys.argv) == 2:
	selection = sys.argv[1]
	print(selection)
else:
	print("Need ext to search for (epub, etc..)")

#Build list of files
listOfFiles = os.listdir('.')
for entry in listOfFiles:
    # if fnmatch.fnmatch(entry, "*."+selection):
	a.append(entry)
	# print(entry)
	
#Convert list 
pattern=('.'+selection)
# print(pattern)
for book in a:
	print(book)
	new_book = (book.replace(pattern, '.mobi'))
	print(new_book)
	# check to see if it has already been converted
	if new_book not in a:
		# convert_book
		pass_arg=[]
		pass_arg.append("ebook-convert")
		pass_arg.append(book)
		pass_arg.append(new_book)
		subprocess.check_call(pass_arg)

			
			
			
			
			
