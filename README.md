# 🎄 Новогодняя Ёлочка с Анимацией Снега 🎄

Этот проект на Python позволяет создать красивую новогоднюю ёлочку прямо в вашем терминале! Вы можете настроить высоту ёлки, частоту украшений, включить цветное отображение и даже добавить анимацию падающего снега. 

## Особенности

- **Настраиваемая высота**: Вы можете задать высоту ёлки, чтобы она идеально вписалась в ваш терминал.
- **Украшения**: Ёлка будет украшена случайными символами, которые можно настроить по частоте появления.
- **Цветное отображение**: Включите цвета, чтобы сделать ёлочку ещё более праздничной.
- **Анимация снега**: Добавьте атмосферу зимнего праздника с помощью анимации падающего снега.

## Установка и запуск

1. Склонируйте репозиторий:
   ```
   git clone https://github.com/kelll31/habr_tree.git
   cd habr_tree
   ```

2. Запустите скрипт с нужными параметрами:
   ```
   python tree.py -r 20 -f 2 -c -s
   ```

   - `-r`, `--rows`: Высота ёлочки (по умолчанию 15).
   - `-f`, `--frequency`: Частота украшений (по умолчанию 3, чем меньше число, тем больше украшений).
   - `-c`, `--colors`: Включить цветное отображение.
   - `-s`, `--snow`: Включить анимацию снега.

## Пример использования

```
python tree.py --rows 20 --frequency 2 --colors --snow
```

Наслаждайтесь праздничным настроением и делитесь радостью с друзьями! С Новым Годом! 🎉

## Лицензия

Этот проект распространяется под лицензией MIT.
