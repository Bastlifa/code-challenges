def reverseInParentheses(inputString):
    s = inputString

    ret_str = ''

    open_count = 0
    open_ind = None
    close_ind = None
    i = 0
    while i < len(s):
        print('i, s[i]', i, s[i])
        if open_count == 0:
            if s[i] != '(':
                ret_str = ''.join([ret_str, s[i]])
                i += 1
            else:
                open_count += 1
                open_ind = i
                close_ind = i
                while open_count > 0:
                    close_ind += 1
                    if s[close_ind] == '(':
                        open_count += 1
                    elif s[close_ind] == ')':
                        open_count -= 1
                ret_str += reverseInParentheses(s[open_ind + 1: close_ind])[::-1]
                i = close_ind + 1
    return ret_str