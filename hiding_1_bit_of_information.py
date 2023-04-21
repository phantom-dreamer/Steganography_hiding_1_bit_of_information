symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main(file_name):
    with open(file=file_name, encoding="utf8") as file_desc:
        lines = file_desc.readlines()

    bit_arrays = []
    index_array = 0

    for line in lines:
        bit_arrays.append([])
        for i in range(len(line)):
            if line[i] in symbols: 
                bit_arrays[index_array].append(1)
            else:
                bit_arrays[index_array].append(0)
        index_array += 1

    print(*bit_arrays, sep = '\n')

    lines_yes = []
    lines_no = []
    index_str = 0
    for bits in bit_arrays:
        result = 0
        for bit in bits:
            result = result | bit
        if result == 1:
            print("Строка " + str(index_str + 1) + ": ДА")
            lines_yes.append(lines[index_str])
        else:
            print("Строка " + str(index_str + 1) + ": НЕТ")
            lines_no.append(lines[index_str])
        index_str += 1
    print('\n')
    print('Строки со скрытой информацией: \n', *lines_yes,)
    print('Строки без скрытой информации: \n', *lines_no,)
 

if __name__ == '__main__':
    print("Метод скрытия с помощью замены символов:")
    main("poem.txt")


