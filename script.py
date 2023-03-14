import json
import fileinput
import shutil

# Define the source and destination file paths
source_file = 'index.html'
destination_file = 'build/code.html'

# Copy the source file to the destination folder
shutil.copyfile(source_file, destination_file)

# Generate the HTML code from JSON data
with open('data.json') as f:
    data = json.load(f)

html = ""
for d in data:
    html += f"""
    <a href={d['link']}>
        <div className="M_ShortcutCard">
            <h1 className="A_CardName"><span className="Q_TextSelection">{d['selected']} </span> {d['text']}</h1>
            <h2 className="A_CardKey">{d['windows']}, {d['macos']}</h2>
        </div>
    </a>
    """

# Replace the target element with the generated HTML code in the destination file
for line in fileinput.input(destination_file, inplace=True):
    if 'id="PYTHON_REPLACE"' in line:
        print(html)
    else:
        print(line, end='')
