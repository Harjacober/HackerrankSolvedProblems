from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data) 
def parse(string):
    parser = MyHTMLParser()
    parser.feed(string)
    parser.close()

n = int(input()) 
parse('\n'.join([input() for _ in range(n)]))   
