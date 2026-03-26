import re, sys

path = r"C:\Users\Luciano\.openclaw\workspace\prompts-site\index.html"
newblock_path = r"C:\Users\Luciano\.openclaw\workspace\prompts-site\newblock.txt"

with open(path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()
with open(newblock_path, 'r', encoding='utf-8') as f:
    newblock = f.read()

pattern = r'"2026-03-26":\s*\[.*?\],?'
if re.search(pattern, content, re.DOTALL):
    new_content = re.sub(pattern, newblock, content, count=1, flags=re.DOTALL)
else:
    start_obj = content.find('const promptsByDay = {')
    if start_obj == -1:
        print("object not found"); sys.exit(1)
    end_obj = content.find('};', start_obj)
    if end_obj == -1:
        print("end object not found"); sys.exit(1)
    before = content[:end_obj]
    after = content[end_obj:]
    # Remove trailing whitespace/comma before inserting
    before_stripped = before.rstrip()
    if before_stripped.endswith(']'):
        before = before_stripped + ',\n' + newblock + before[len(before_stripped):]
    else:
        before = before + newblock
    new_content = before + after

with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
