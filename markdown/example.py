import codecs
import markdown
from pprint import pprint

# pprint(dir(markdown))
my_markdown = '''
* Markdown
* Wiki markup
* HTML
'''
pprint(markdown.markdown(my_markdown))

# print example
with codecs.open('example.md', mode='r', encoding='utf-8') as f:
  html = markdown.markdown(f.read())

# pprint(html)
with codecs.open('example.html', mode='w', encoding='utf-8') as f:
  f.write(html)


