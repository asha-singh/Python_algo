
def selectionSort(input_list):
    list_length = len(input_list)
    
    for i in range(list_length):
        min = i
        for j in range(i+1, list_length):
            if input_list[j]<input_list[min]:
                min=j
       
        input_list[min], input_list[i] = input_list[i] , input_list[min]
        
    return  input_list   




        


