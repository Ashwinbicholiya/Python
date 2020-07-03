import textwrap

def wrap(string, max_width):
    string = textwrap.fill(string,4)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)