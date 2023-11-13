

def reverse_list(input_list):
    if not input_list:
        return []
    if len(input_list) == 1:
        return [input_list[0]]
    else:
        return reverse_list(input_list[1:]) + [input_list[0]]

    pass



if __name__ == "__main__":

    liste = [1,3,5,6]

print(reverse_list(liste))