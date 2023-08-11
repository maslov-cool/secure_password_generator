def passwords():
    print("                **    **  ********  **        **            **      ")
    print("               **    **  ********  **        **         **     **   ")
    print("              ********  **        **        **         **      **  ")
    print("             ********  ********  **        **         **      **  ")
    print("            **    **  **        **        **         **      **  ")
    print("           **    **  ********  ********  ********    **    **   ")
    print("          **    **  ********  ********  ********       **      ")
    import random
    digits = '0123456789'
    big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!#$%&*+-=?@^_'
    chars = ''
     
    def is_valid_(s):
            if str(s).isdigit():
                return True
            return False
            
     
    def start():
        while True:
            quantity = input('Здравствуйте, сколько паролей вам сгенерировать?')
            if is_valid_(quantity):
                quantity = int(quantity)
                break
            elif not is_valid_(quantity) or quantity == '':
                print('А может быть все-таки введем целое число?')
                continue
            
        while True:
            length = input('Напишите длину пароля(или паролей) для генерации: ')
            if is_valid_(length):
                length = int(length)
                break
            elif not is_valid_(length) or length == '':
                print('А может быть все-таки введем целое число?')
                continue
            elif int(len) > len(digits + symbols + big_letters + small_letters):
                print('Такая длина недопутима, может сделайте её покороче')
                continue
            
        while True:
            have_digit = input('Включать ли цифры 0123456789? Введите "да" или "нет"')
            if have_digit.lower() == 'да' or have_digit.lower() == 'нет':
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
        
        while True:
            have_big_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите "да" или "нет"')
            if have_big_letters.lower() == 'да' or have_big_letters.lower() == 'нет':
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
        
        while True:
            have_small_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите "да" или "нет"')
            if have_small_letters.lower() == 'да' or have_small_letters.lower() == 'нет':
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
        
        while True:
            have_symbols = input('Включать ли символы !#$%&*+-=?@^_? Введите "да" или "нет"')
            if have_symbols.lower() == 'да' or have_symbols.lower() == 'нет':
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
        
        while True:
            have_similar_symbols = input('Исключать ли неоднозначные символы il1Lo0O? Введите "да" или "нет"')
            if have_similar_symbols.lower() == 'да' or have_similar_symbols.lower() == 'нет' :
                generate_password(length, quantity, chars, have_digit, have_big_letters, have_small_letters, have_symbols, have_similar_symbols)
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
            
            
    def generate_password(length, quantity, chars, have_digit, have_big_letters, have_small_letters, have_symbols, have_similar_symbols):
        print()
        while True:
            if len(chars) > length:
                break
            if have_digit == 'да':
                chars += digits
                
            if have_big_letters == 'да':
                chars += big_letters
                
            if have_small_letters == 'да':
                chars += small_letters
                
            if have_symbols == 'да':
                chars += symbols
                
            if have_symbols == 'да':
                for i in chars:
                    if i in 'il1Lo0O':
                        chars.replace(i, '')
        for i in range(quantity):
            print(f'Пароль {i + 1}:')
            print(*random.sample(chars, length), sep = '')
            print()
        continue_generate()
        
        
    def continue_generate():
        while True:
            restart = input('Нужно ли вам ещё сгенерировать пароли? (Введите "да" или "нет"): ')
            if restart.lower() == 'да':
                start()
            elif restart.lower() == 'нет':
                print("                 *******   **     **    ********")
                print("                *******     **   **    ********")
                print("               **   **       ** **    ***       ")
                print("              ******          ***    ********")
                print("             ******           **    ********")
                print("            **   **          **    ***     ")
                print("           ********         **    ********")
                print("          ********         **    ********")
                break
            else:
                print('Я не понимаю. Введите "да" или "нет"')
                continue
        
    start()
    
passwords()