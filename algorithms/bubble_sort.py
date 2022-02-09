

def bubbleSort(input_list):
    list_length = len(input_list)
    for i in range(list_length):
        for j in range(list_length-1):
            if input_list[j] > input_list[j+1]:
                tmp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = tmp

    return input_list

"""
def main():
    test_array = [3, 5, 4, 1, 2]
    print(bubbleSort(test_array))


if __name__ == "__main__":
    main()
"""