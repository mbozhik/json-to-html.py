import json

with open('data.json') as f:
    data = json.load(f)

html = ""
for d in data:
    html += f"""
    <a href={d['link']}>
        <div className="M_ShortcutCard">
            <h1 className="A_CardName"><span className="Q_TextSelection">{d['selected']} </span> {d['text']}</h1>
            <h2 className="A_CardKey">{d['windows'], d['macos']}</h2>
        </div>
        </a>
    """

with open('build.html', 'w') as f:
    f.write(html)