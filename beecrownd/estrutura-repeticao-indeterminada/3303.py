while True:  
    try:
        palavra = input()
        if len(palavra) > 20 or not palavra.islower():
            continue
        if len(palavra) >= 10:
            print('palavrao')
        else:
            print('palavrinha')
    except:
        break

                      