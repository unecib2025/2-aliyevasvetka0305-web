1
password=''
while password !='admin123':
    password=input('Введите пароль:')
print('Доступ разрешен')

2
login=input('Введите логин')
while len(login)< 6:
    print('Логин слишком короткий')
    login=input('Введите логин заново:')
print('Логин принят')

3
correct_password = "admin123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Введите пароль: ")
    if password == correct_password:
        print("Вход выполнен успешно")
        break
    else:
        print("Неверный пароль")
        attempts += 1

if attempts == max_attempts:
    print("Доступ заблокирован")

4
for i in range(1, 11):
    print(f"Запись журнала №{i}")

5
hashes_original = ["1a", "2b", "3c", "4d"]
hashes_current = ["1a", "2x", "3c", "4d"]

for i in range(len(hashes_original)):
    if hashes_original[i] == hashes_current[i]:
        print(f"Файл {i + 1} не изменён")
    else:
        print(f"Файл {i + 1} повреждён")
