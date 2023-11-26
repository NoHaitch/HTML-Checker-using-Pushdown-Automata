def validate_html(html):
    stack = []
    state = 'Q0'

    transitions = {
        ('Q0', '<html'): 'a',
        ('Q0', '>'): 'b',
        ('Q1', '</html>'): 'b',
        ('b', '>'): 'c'
    }

    for char in html:
        if state == 'Z':
            break

        if (state, char) in transitions:
            new_state = transitions[(state, char)]

            if new_state == 'a':
                stack.append(char)
            elif new_state == 'b':
                if new_state == 'b' and stack and stack[-1] == '<':
                    stack.pop()
                else:
                    return False
            state = new_state
        else:
            return False

    return state == 'Z' and not stack

# Test the function
html_str = "<html><body>Hello</body></html>"
result = validate_html(html_str)

if result:
    print("The HTML is valid.")
else:
    print("The HTML is not valid.")
