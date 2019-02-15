import re
import sys

def remove_comments(text):
    """ remove c-style comments.
        text: blob of text with comments (can include newlines)
        returns: text with comments removed
    """
    pattern = r"""
                            ##  --------- COMMENT ---------
           /\*              ##  Start of /* ... */ comment
           [^*]*\*+         ##  Non-* followed by 1-or-more *'s
           (                ##
             [^/*][^*]*\*+  ##
           )*               ##  0-or-more things which don't start with /
                            ##    but do end with '*'
           /                ##  End of /* ... */ comment
         |                  ##  -OR-  various things which aren't comments:
           (                ##
                            ##  ------ " ... " STRING ------
             "              ##  Start of " ... " string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^"\\]       ##  Non "\ characters
             )*             ##
             "              ##  End of " ... " string
           |                ##  -OR-
                            ##
                            ##  ------ ' ... ' STRING ------
             '              ##  Start of ' ... ' string
             (              ##
               \\.          ##  Escaped char
             |              ##  -OR-
               [^'\\]       ##  Non '\ characters
             )*             ##
             '              ##  End of ' ... ' string
           |                ##  -OR-
                            ##
                            ##  ------ ANYTHING ELSE -------
             .              ##  Anything other char
             [^/"'\\]*      ##  Chars which doesn't start a comment, string
           )                ##    or escape
    """


    p = r'/\*[^*]*\*+([^/*][^*]*\*+)*/|("(\\.|[^"\\])*"|\'(\\.|[^\'\\])*\'|.[^/"\'\\]*)'


    multi_str = ''.join(m.group(2) for m in re.finditer(p, text, re.M|re.S) if m.group(2))
    #print(ret_str)

    multi_list = multi_str.split('\n')
    #print(multi_list)

    single = []
    for sentence in multi_list:
        if sentence.startswith('??'):
            single.append(sentence)
            multi_list.remove(sentence)

    #print(multi_list)
    #print(single)

    s = '\n'.join(x for x in multi_list)
    final = '\n'.join([i for i in s.split('\n') if len(i) > 0])

    print(final)
    return final




'''
    pr = re.compile(r'\?\?[^\n\r]+?(?:\*\)|[\n\r])')
    ss = pr.search(ret_str)
    print(ss)
    final = ''.join(m.group() for m in pr.finditer(ret_str) if m.group())
    print(final)
'''


# list comprehension explained
'''
    for m in pr.finditer(text):
        if m.group():
            print("text is: " + m.group() + "indices are: " + str(m.span()))

    print(m)
'''



'''
# save comments in another file : FAILED

for m in re.finditer(p, text, re.M|re.S):
    if m.group():
        print("text is: " + m.group() + "indices are: " + str(m.span()))

print(m)
for m in re.finditer(p, text, re.M|re.S):
    print(m)
    print("text : " + "%r"%m.group() + "indices are : " + str(m.span()))
'''


# multi line comment explained
'''
    regex = re.compile(pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    noncomments_multi = [m.group(2) for m in regex.finditer(text) if m.group(2)]

    partial = "".join(noncomments_multi)

    print(partial)

    return partial
'''



'''
    single_line_pattern = r"""
            ^\?\?[ a-z]*
    """

    single_regex = re.compile(single_line_pattern, re.VERBOSE|re.MULTILINE|re.DOTALL)
    nocomments = [m.group() for m in single_regex.finditer(partial) if m.group()]

    return "".join(nocomments)


    for m in single_regex.finditer(text):
        if m.group():
            print("text is: " + m.group() + "indices are: " + str(m.span()))

        print(m)
    print("Done single")
'''



# can be run separately
'''
if __name__ == '__main__':
    filename = sys.argv[1]
    code_w_comments = open(filename).read()
    code_wo_comments = remove_comments(code_w_comments)
    fh = open(filename+".nocomments", "w")
    fh.write(code_wo_comments)
    fh.close()
'''
