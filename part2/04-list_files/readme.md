# Работа с файлами и потоками данных  

**Л/Р 5 - 31.03.22**  
за основу можно брать проги из папки **02-rec_que_walk**  

**Задачи:**  

Создайте папку /public/  и в ней поместите 2-3 текстовых файла, в файлах можете разместить пару строчек текста  

> 1) вывести на экран список файлов из папки public (не включать вложенные директории и файлы из них)  

> 2) вывести на экран список файлов из папки public, отсортировав их по размеру по возрастанию  

> 3) предварительно (руками) сделайте в папке public пару временных директорий и там создайте по 2-3 файла с расширением **.ini**  
> Задание для программы: найти все файлы в текущей папке (где лежит сама программа) и во всех её поддиректориях по фильтру: расширение файла **.ini** и поменять у таких файлов на расширение **.cfg** (самостоятельно найдите метод для переименования файлов)  

> 4) найти все файлы в папке public и во всех её поддиректориях по фильтру: расширение файла **.cfg** и добавить последней строкой к содержимому каждого файла значение параметра - имя самого файла (без пути) по шаблону:

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
