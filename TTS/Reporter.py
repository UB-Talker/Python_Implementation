from datetime import datetime


def formatted_timestamp():
    return str(datetime.now()).replace(' ', '_').split('.').pop(0)


def conversation_parse_filter(c):
    if c == ' ':
        return True
    return c.isalnum()


def word_count_comparator(item):
    word, count = item
    return count


def init_private_vars():
    global report_name
    report_name = 'TTS/conversations/' + formatted_timestamp() + '.txt'
    init_word_count()
    global report_doc
    report_doc = open(report_name, 'w')


def init_word_count():
    global word_count
    word_count = {}
    try:
        stats = open('TTS/stats/word_count.txt', 'r')
        for line in stats:
            item = line.split(',')
            count = int(item.pop())
            word = item.pop()
            word_count[word] = count
        stats.close()
    except FileNotFoundError:
        print('No word_count file found')
    pass


def update_word_count():
    report_ref = open(report_name, 'r')
    for line in report_ref:
        line = line.split('\t').pop()
        line = ''.join(c for c in line if conversation_parse_filter(c))
        words = line.split(' ')
        for word in words:
            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    report_ref.close()
    pass


def save_word_count():
    stats = open('TTS/stats/word_count.txt', 'w')
    for word, count in sorted(word_count.items(), key=word_count_comparator, reverse=True):
        stats.write(word + ',' + str(count) + '\n')
    stats.close()
    pass


def report(text):
    report_doc.write(formatted_timestamp() + '\t' + text + '\n')
    pass


def close_report():
    report_doc.close()
    update_word_count()
    save_word_count()
    pass


init_private_vars()
