from pathlib import Path
import sys


def sub(text, components):
    """Replace the components in the text."""
    for key, value in components.items():
        text = text.replace(f"{{{key}}}", f"{key.upper().replace('_', ' ')}:\n" + value)
    return text


def write(text, fname):
    """Write the text to the file."""
    with open(fname, "w", encoding="utf8") as f:
        f.write(text)
    print(f"Wrote {fname}")


mode = "normal"
if len(sys.argv) > 1:
    mode = sys.argv[1]

if mode == "normal":
    template_file = "templates/TEMPLATE.txt"
else:
    template_file = "templates/TEMPLATE_PER_UNIT.txt"

# read the components
components = {}
for file in Path("components").glob("*.txt"):
    with open(file, "r", encoding="utf8") as f:
        components[file.stem] = f.read()

# read the template
with open(template_file, "r", encoding="utf8") as f:
    template = f.read()

if mode != "normal":
    # replace the components
    for unit in range(1, 10):
        unit_name = "unit_" + str(unit)
        if unit_name in components:
            components["units"] = components[unit_name]
            template = sub(template, components)
            # write the output
            write(template, f"units/DFHBOT_UNIT_{unit}.txt")

else:
    # replace the components
    template = sub(template, components)
    # write the output
    write(template, "DFHBOT.txt")
