def split_and_join(line):
    newline = ""
    newline = line.split(" ")
    newline = "-".join(newline)
    return newline

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
