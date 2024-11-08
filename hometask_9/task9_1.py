def popular_words (text, words):
	text_word_list = text.lower().split()
	word_list = []

	for word in words:
		word_count = text_word_list.count(word)
		word_list.append((word, word_count))

	return dict(word_list)


print(popular_words('When I was One I had just begun When I was Two I was nearly new', ['i', 'was', 'three', 'near']))

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
