



def input_output(entry):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for x in entry:
        if x[0] in vowels:
            print(",".join(entry)+ "way")
        elif x[0] not in vowels:
            pass          
        else:
            pass

entry = [x for x in input("Enter a word:").split(',')]
input_output(entry)
clear
