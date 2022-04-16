# Работа с файлами и потоками данных  

**Л/Р 5 - 31.03.22**  

**Задачи:**  

> 1) вывести на экран список файлов из текущей папки (не включать вложенные директории и файлы из них)  

> 2) вывести на экран список файлов из текущей папки, отсортировав их по размеру по возрастанию  

> 3) предварительно (руками) сделать в текущей папке пару временных директорий и там создать по 2-3 файла с расширением **.ini**  
> Задание для программы: найти все файлы в текущей папке (где лежит сама программа) и во всех её поддиректориях по фильтру: расширение файла **.ini** и поменять у таких файлов на расширение **.cfg**  

> 4) найти все файлы в текущей папке (где лежит сама программа) и во всех её поддиректориях по фильтру: расширение файла **.cfg** и добавить последней строкой к содержимому каждого файла значение параметра - имя самого файла (без пути) по шаблону:
```
name_file: <имя файла>
```
Например, если был файл config.cfg и у него внутри были такие строчки:
```txt
date: 2022.03.31
list_avg: 1024.666
```
то после работы программы в этом файле будет следующее содержимое:
```txt
date: 2022.03.31
list_avg: 1024.666
name_file: config.cfg
```

В исходные файлы можете сами написать (придумать) какие-нибудь параметры (2-3 штуки)...

---  

---  