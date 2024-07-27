list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search_1(list2 , number):
    start_list = 0
    end_of_list = len(list2) - 1

    while start_list <= end_of_list:
        half = (end_of_list + start_list) / 2
        half = int(half)
        assumption = list2[half]

        if assumption > number:
            end_of_list = half - 1

        elif assumption < number:
            start_list = half + 1

        elif assumption == number:
            return assumption





print(binary_search_1(list1,1))