import re
# re.search() checks for a match ANYWHERE in the string.
line = "Cats are smarter than dogs"
search_obj = re.search(r'dogs', line)
if search_obj:
    print("re.search found:", search_obj.group())
