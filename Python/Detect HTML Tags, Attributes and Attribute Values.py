# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1])) 
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
def parse(string):
    parser = MyHTMLParser()
    parser.feed(string)
n = int(input())
parse(''.join([input() for _ in range(n)]))
