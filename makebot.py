from pathlib import Path
import sys


if len(sys.argv)>1:
    template_file = sys.argv[1]
else:
    template_file = 'makebot/TEMPLATE.txt'

# read the components 
components = {}
for file in Path('makebot').glob('*.txt'):
    with open(file, 'r', encoding="utf8") as f:
        components[file.stem] = f.read()


# read the template
with open(template_file, 'r', encoding="utf8") as f:
    template = f.read()

# replace the components
for key, value in components.items():
    template = template.replace(f'{{{key}}}', f"{key.upper().replace('_', ' ')}:\n"+value)

# write the output
with open('DFHBOT.txt', 'w', encoding="utf8") as f:
    f.write(template)

