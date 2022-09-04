import textwrap

def wrap(string, max_width):
    hasil = textwrap.fill(string, max_width)
  # hasil = textwrap.wrap(string, max_width) ~~~~ hasil dalam list
    return hasil

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
