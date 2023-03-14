import json
import fileinput

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

for line in fileinput.input('shortcuts.html', inplace=True):
    if 'id="PYTHON_REPLACE"' in line:
        print(html)
    else:
        print(line, end='')