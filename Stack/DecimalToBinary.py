from stack import Stack



def convert_int_to_bin(dec_num):
    s = Stack()
    number = dec_num
    binary_number = ""

    if dec_num == 0:
        return 0

    while number !=0:
        if number % 2 == 0:
            s.push('0')
            number = int(number/2)
        else:
            s.push('1')
            number =  int(number / 2)

    while not s.is_empty():
        binary_number +=s.pop()

    return binary_number


print(convert_int_to_bin(9))