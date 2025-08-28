import random

def generate_lists():
    list1= []
    list2=[]
    list1_length = random.randint(0, 20)
    list2_length = random.randint(0, 20)
    for i in range(list1_length):
        list1.append(random.randint(0, 99))
    
    for i in range(list2_length):
        list2.append(random.randint(0, 99))
     
    print(f' List 1 is: {list1} \n list2 is: {list2}')
    return list1, list2

def print_unique_nums(list1, list2):
    final_list = []
    for i in list1:
        for j in list2:
            if i == j and i not in final_list:
                final_list.append(i)
    if (len(final_list) != 0):
        print(f'The numbers that are present in both of the lists are: {final_list}')
    else:
        print("There were no matching numbers between the two lists.")

list1, list2 = generate_lists()
print_unique_nums(list1, list2)