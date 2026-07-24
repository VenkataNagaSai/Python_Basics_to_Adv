import re
# Parsing layout coordinate files
line = "BlockA -x1 10 -x2 50 -y1 10 -y2 50"
match = re.match(r'(.*)-x1 (.*) -x2 (.*) -y1 (.*) -y2 (.*)', line)
if match:
    area = (int(match.group(3)) - int(match.group(2))) * (int(match.group(5)) - int(match.group(4)))
    print(f"Area of {match.group(1).strip()} is {area}")
