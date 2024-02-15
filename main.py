def file_open(path):
    try:
        with open(path, 'r') as file:
            file_contents = file.read()
    except PermissionError as e:
        print(e)

    return file_contents

def main():
    data = {'1.txt': [],
            '2.txt': [],
            '3.txt': []}

    while True:
        txt_1 = file_open('1.txt').split(' ')
        txt_2 = file_open('2.txt').split(' ')
        txt_3 = file_open('3.txt').split(' ')

        word = input("Enter the word(@ for quit): ")
        if word == '@':
            break
        if not word.isalpha():
            print("Enter word without special characters!")
            continue
        
        for i in range(len(txt_1)):
            if word in txt_1[i] and len(word) == len(txt_1[i]):
                print(f'\'{word}\' is in 1.txt!')
                break
        for i in range(len(txt_2)):
            if word in txt_2[i] and len(word) == len(txt_2[i]):
                print(f'\'{word}\' is in 2.txt!')
                break
        for i in range(len(txt_3)):
            if word in txt_3[i] and len(word) == len(txt_3[i]):
                print(f'\'{word}\' is in 3.txt!')
                break

if __name__ == '__main__':
    main()
