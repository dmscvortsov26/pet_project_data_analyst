def shifr_en(sdvig, n):
    res = ""
    for el in n:
        if el.isalpha():
            fn = ord(el) - sdvig
            if (el.islower() and 97 <= fn <= 122) or (el.isupper() and 65 <= fn <= 90):
                res += chr(fn)         
            else:
                fn = (ord(el) - sdvig) + 26
                res += chr(fn) 
        else:
            res += el        
    return res


def shifr_ru(sdvig, n):
    res = ""    
    for el in n:
        if el.isalpha():
            fn = ord(el) - sdvig
            if (el.islower() and 1072 <= fn <= 1103) or (el.isupper() and 1040 <= fn <= 1071):
                res += chr(fn)  
            else:
                fn = (ord(el) - sdvig) + 32
                res += chr(fn) 
        else:
            res += el          
    return res  


def deshifr_en(sdvig, n):
    res = ""
    for el in n:
        if el.isalpha():
            fn = ord(el) + sdvig
            if (el.islower() and 97 <= fn <= 122) or (el.isupper() and 65 <= fn <= 90):
                res += chr(fn) 
            else:
                fn = (ord(el) + sdvig) - 26
                res += chr(fn)
        else:
            res += el     
    return res  


def deshifr_ru(sdvig, n):
    res = ""
    for el in n:
        if el.isalpha():
            fn = ord(el) + sdvig
            if (el.islower() and 1072 <= fn <= 1103) or (el.isupper() and 1040 <= fn <= 1071):
                res += chr(fn)
            else:
                fn = (ord(el) + sdvig) - 32
                res += chr(fn)
        else:
            res += el   
    return res   


def terminal():
    flag = True
    while flag:
        print("Здравствуйте")

        print("1. Шифрование")
        print("2. Дешифрование") 
        print("3. Выход")

        print("ВЫБЕРИТЕ ДЕЙСТВИЕ 1, 2, 3")
        text = input() 

        if text == "3":
            print("До свидания")
            flag = False
            continue

        if text in ["1", "2"]:
            print("Выберите язык: 1 - en, 2 - ru")
            language = input()
            print("Сдвиг в шифре = ")
            sdvig = int(input())
            print("Ваш текст...")
            new_text = input()

            if text == "1":
                if language == "1":
                    result = shifr_en(sdvig, new_text)
                else:
                    result = shifr_ru(sdvig, new_text)
                print(f"Зашифрованный текст: {result}")

            else:
                if language == "1":
                    result = deshifr_en(sdvig, new_text)
                else:
                    result = deshifr_ru(sdvig, new_text)
                print(f"Расшифрованный текст: {result}")
        
        else:
            print("Неверный выбор, допустимые значения 1 или 2, попробуйте снова")


terminal()
