# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for attr in attrs:
            print("->",attr[0],">",attr[1])
    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for attr in attrs:
            print("->",attr[0],">",attr[1])
def parse(string):
    parser = MyHTMLParser()
    parser.feed(string)

arr = []
n = int(input())
for i in range(n):
    arr.append(input())
parse('\n'.join(arr))    
