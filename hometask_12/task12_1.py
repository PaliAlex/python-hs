import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    string_list = []

    with open(html_file, "r", encoding="utf-8") as html_file:
        for line in html_file:
            text = re.findall(r'[h1, p]>([А-Яа-яЁёІіЇїЄєҐґ\s—\-!?.,]*)<', line)
            if len(text) > 0:
                string_list.append(text[0])

    with open(result_file, "w") as test_file:
        for text in string_list:
            test_file.write(text + '\n')

delete_html_tags('draft.html', 'cleaned.txt')

