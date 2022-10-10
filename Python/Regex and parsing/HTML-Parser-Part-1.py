from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("Start :", tag)
    for name, value in attrs:
      print("-> {} > {}".format(name, value))
  def handle_endtag(self, tag):
    print("End   :",tag)
  def handle_startendtag(self, tag, attrs):
    print("Empty :",tag)
    for name, value in attrs:
      print("-> {} > {}".format(name, value))

parser = MyHTMLParser()
for i in range(int(input())):
  parser.feed(input())
parser.close()
