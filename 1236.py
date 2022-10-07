import random
def is_valid(n):
    if n.isdigit() and 0 < int(n) < 101:
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку')
print('Введите число от 1 до 100')

flag = True
while flag == True:
    a = random.randint(1, 100)
    while True:
        n = input()
        if is_valid(n) == True:
            n = int(n)
            if n > a:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            if n < a:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            if n == a:
                print('Вы угадали, поздравляем! \n')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    
    print('Может быть сыграет ещё?   Да/Нет')
    end = input()
    if end.lower() == 'да':
        print('Отлично! Я загадал новое, число попробуй отгадай его! \n')
        flag = True
    else: 
        flag = False
        print('До скорой встречи!')        


   
