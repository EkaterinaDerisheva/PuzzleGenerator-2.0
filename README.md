# PuzzleGenerator-2.0
Новая версия генератора шахматных задач на основе библиотеки python-chess

## О Приложении
Генератор шахматных задач - это консольное приложение, написанное на языке Python, которое позволяет создавать похожие шахматные задачи на основе одной из нескольких сотен тысяч задач на тему "Мат в 2 хода", которые хранятся в базе задач "MateIn2WithLevel.csv". Новые задачи получаются из данной путём смены положения на доске ключевых, для решения задачи, фигур игрока и изменения их типа. Каждая полученная задача имеет свой уникальный идентификатор, FEN и набор ходов. Все задачи в базе проранжированны по уровню сложности от 1 до 8.
## Как пользоваться генератором? 
### Установка и запуск приложения:
1. Скачайте файлы "setup.sh", "run.sh", "requirements.txt" на свой компьютер и поместите их в директорию, в которой хотите видеть папку с проектом
2. Откройте консоль и введите следующие команды:
3. ```bash path/to/setup.sh``` чтобы установить проект
4. ```bash path/to/run.sh``` чтобы запустить проект на локалхосте
### Генерация задач:
1. Отправьте POST-запрос с ID оригинальной задачи, содержащий body вида { "id": "<id_задачи>" }, на локалхост http://127.0.0.1:5000/generate-puzzles
2. Сервер вернет массив сгенерированных задач в виде JSON-ов с полями ID, Fen, Moveset и Level
