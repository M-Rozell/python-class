# python module_1.py command to run in cmder

lst_1 = [3,2,6]
lst_2 = [4,9,3]
lst_3 = [9,6,3]
lst = [lst_1, lst_2, lst_3]
print(lst)

elements = [[3,2,6], [4,9,3], [9,6,3]]
print(elements[0][0], elements[1][2], elements[2][1])



def extract_from_list(elements):
    result = [elements[0][0], elements[1][2], elements[2][1]]
    return result
print(extract_from_list([[3,2,6], [4,9,3], [9,6,3]]))

# def extract_from_list(elements):
    
#     for i in elements:
#         print(i[0])
#         for t in i:
#             print(t[0])
            
# print(extract_from_list([[3,2,6], [4,9,3], [9,6,3]]))





def count_e_in_string(string):
    count = 0
    for c in string:
        if c == "e":
          count = count + 1
    return count
print(count_e_in_string("Hello enter"))          


def count_l_in_string(string):
    count = 0
    for c in string:
        if c == "l":
            count = count + 1
    return count
print(count_l_in_string("Hello"))
   



def length_of_string(string):
    return len(string)
print(length_of_string("Iamsix"))




def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello World!!"))


def reverse_string(string):
    return "".join(reversed(string))
print(reverse_string("Hello World"))




def concact_elements_in_list(elements):
    new_string = ""
    for c in elements:
           new_string += c + " "
    return new_string
print(concact_elements_in_list(["This", "is", "my", "string."]))


my_list = ["This", "is", "my", "string."]
new_string = ""
for c in my_list:
    new_string += c + " "
print(new_string)



def sum_characters_in_list(elements):
    lst = []
    for c in range(1,6):
        lst.append(c)
    return sum(lst)
print(sum_characters_in_list([1,2,3,4,5]))

my_second_list = [1,2,3,4,5]
lst = []
for c in range(1,6):
    lst.append(c)
print(sum(lst))

   
