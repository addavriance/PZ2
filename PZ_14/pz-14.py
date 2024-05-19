"""
Вариант 19
Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
Посчитать их количество.
"""

import re

with open("../assets/pazzl.html") as f:
    text = f.read()
    img_tags = re.findall(r"<img[^>]*>", text)
    print(*img_tags)
    print(f"Количество тегов 'img': {len(img_tags)}")