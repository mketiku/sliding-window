#!/usr/bin/env python2

def window(input):
    iterable = list(input)
    result = []

    if len(iterable) < 1:
        result = [(iterable, None)]
    else:
        for index, element in enumerate(iterable):
            if index < (len(iterable) - 1):
                result.append((element, iterable[index + 1]))
            else:
                result.append((element, None))
    return(result)

