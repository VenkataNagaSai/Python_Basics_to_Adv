import re
# split() breaks strings into lists. sub() replaces patterns.
txt = "The rain in Spain"
print("Split:", re.split(r"\s", txt))
phone = "2004-959-559 # Phone Number"
print("Sub (remove comments):", re.sub(r'#.*$', "", phone))
