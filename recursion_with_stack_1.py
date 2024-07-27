def fibonachi(before_end,end):
    if before_end == 0:
        return 0

    else:

        return before_end , end , fibonachi(end-before_end,before_end)


print(fibonachi(13,21))