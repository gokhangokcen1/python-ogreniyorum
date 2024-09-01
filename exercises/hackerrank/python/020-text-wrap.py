import textwrap

def wrap(string, max_width):
    # OR
    """
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text
    """
    wrapped_text = ""
    
    for i in range(0, len(string), max_width):
        wrapped_text += string[i:i+max_width] + "\n"
    
    return wrapped_text

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)