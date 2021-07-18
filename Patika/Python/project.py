def flatten(l):

    output = []

    def get_item(l):

        for item in l:
            if type(item) == list:
                get_item(item)
            else:
                print(type(item),item)
                output.append(item)
    
    get_item(l)

    return output

def reversal(l):

    output = []

    def get_reverse(l):
        sub = []
        for item in reversed(l):
            if type(item) == list:
                get_reverse(item)
            else:
                sub.append(item)
        if len(sub) != 0:
            output.append(sub)

    get_reverse(l)

    return output
