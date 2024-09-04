import re

italics = re.compile(r'<em>(.+?)</em>')
spaces = re.compile(r'\s+')
paragraph = re.compile(r'<p>(.+?)</p>')
urls = re.compile(r'<a href="(.+?)">(.+?)</a>')

# test_string = 'This is the <a href="https://pypi.org/project/html2markdown/">link</a> to the html2markdown package.'

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    # TODO: 
        # Convert <em> </em> tags to *
        # Strip any whitespace or \n to just single space
        # Convert <p> tags to have \n\n between
        # Convert url a tags to []() format
    markdown = italics.sub(r'*\1*', html)
    markdown = spaces.sub(r' ', markdown)
    markdown = paragraph.sub(r'\1\n\n', markdown)
    markdown = urls.sub(r'[\2](\1)', markdown)
    
    return markdown.strip()

# print(html2markdown(test_string))