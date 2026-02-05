import os

# Файлы, где ищем контракт
FILES_TO_UPDATE = ['chart.html', 'sloth.html', 'test.html', 'swap.html']

# Старый контракт (один из двух — выбирай сам)
OLD_CA = '71Jvq4Epe2FCJ7JFSF7jLXdNk1Wy4Bhqd9iL6bEFELvg'

def заменить_в_файле(файл, старый, новый):
    if not os.path.exists(файл):
        print(f"Не нашёл файл: {файл}")
        return
    
    with open(файл, 'r', encoding='utf-8') as f:
        текст = f.read()
    
    обновлённый = текст.replace(старый, новый)
    
    with open(файл, 'w', encoding='utf-8') as f:
        f.write(обновлённый)
    
    print(f"✓ {файл} — заменил '{старый}' на '{новый}'")

def запуск():
    новый_ca = input(f"Новый контракт (оставь пусто — будет {OLD_CA}): ").strip()
    if not новый_ca:
        новый_ca = OLD_CA
    else:
        # Если ввёл другой — меняем
        for файл in FILES_TO_UPDATE:
            заменить_в_файле(файл, OLD_CA, новый_ca)

if __name__ == "__main__":
    запуск()