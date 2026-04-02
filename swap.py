import sys

file_path = r"c:\Users\HP\Desktop\iron fitness\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the exact indices instead of hardcoding just in case
def find_index(content, text):
    for i, line in enumerate(content):
        if text in line:
            return i
    return -1

pricing_start = find_index(lines, "<!-- 3. MEMBERSHIP / FEES SECTION -->")
pricing_end = find_index(lines[pricing_start:], "</section>") + pricing_start

trainer_start = find_index(lines, "<!-- 4. TRAINER / FOUNDER SECTION -->")
trainer_end = find_index(lines[trainer_start:], "</section>") + trainer_start

pricing_block = lines[pricing_start:pricing_end+1]
trainer_block = lines[trainer_start:trainer_end+1]

# Adjust classes for alternating backgrounds
for i, line in enumerate(pricing_block):
    if '<section class="section"' in line and 'bg-dark' not in line:
        pricing_block[i] = line.replace('class="section"', 'class="section bg-dark"')
    if '<!-- 3. MEMBERSHIP' in line:
        pricing_block[i] = line.replace('3.', '4.')

for i, line in enumerate(trainer_block):
    if '<section class="section bg-dark"' in line:
        trainer_block[i] = line.replace('class="section bg-dark"', 'class="section"')
    if '<!-- 4. TRAINER' in line:
        trainer_block[i] = line.replace('4.', '3.')

# Construct new array of lines
new_lines = lines[:pricing_start] + trainer_block + ["\n"] + pricing_block + lines[trainer_end+1:]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Swapped successfully")
