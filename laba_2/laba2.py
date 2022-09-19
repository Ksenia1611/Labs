#Сортировка простым выбором 

def selection_sort(list):
    for i in range(0, len(list) - 1):
        min_letter = list[i]
        min = i
        for j in range(i + 1, len(list)):
            if list[j] <  min_letter:
                min_letter = list[j]
                min = j
        list[min] = list[i]
        list[i] = min_letter
    print(list)
 
 
list = input('Введите список чисел: ').split()
list = [int(x) for x in list]
selection_sort(list) 