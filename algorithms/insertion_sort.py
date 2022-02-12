def insertionSort(input_list):
    input_length = len(input_list)
    for i in range(1, input_length):
        j = i-1
        temp = input_list[i]
        while(j>=0 and input_list[j]>temp ):
            input_list[j+1]=input_list[j]
            j=j-1
        input_list[j+1]=temp   
    return  input_list



