# -*- coding: utf-8 -*-
with open('js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = "currentModuleId: 'mod-0',"
replacement = "currentModuleId: (typeof MODULES_DATA !== 'undefined' && MODULES_DATA.length > 0) ? MODULES_DATA[0].id : 'mod-joy-0',"

if target in text:
    text = text.replace(target, replacement)
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated currentModuleId dynamically.")
else:
    print("Target string not found or already updated.")
