# SQL

## Введение в язык структурированных запросов SQL

Предполагается, что данные распределены по таблицам и могут иметь логические связи между полями таблиц.  

Синтаксис SQL включает несколько категорий команд, основные из них:  

1) DDL – язык определения данных (Data Definition Language) - для декларации структуры таблиц;  
2) DML – язык манипулирования данными (Data Manipulation Language)- для изменения записей в таблицах;  
3) DQL – язык запросов (Data Query Language) - для выборки данных из таблиц;  
4) DCL – язык управления данными (Data Control Language) - для управления доступом к таблицам.  

Начальный уровень подготовки по реляционным базам данных можно ограничить:  
Подмножеством команд DQL:  
SELECT  
Подмножеством команд DML:  
INSERT, UPDATE, DELETE  
Подмножеством команд DDL:  
CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX, ALTER INDEX, DROP INDEX  

Примеры команд:

```SQL
CREATE TABLE `students` (
  `id` int NOT NULL,
  `nameStud` varchar(20) NOT NULL,
  `rating` int NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `date` date NOT NULL,
  `city` varchar(20) NOT NULL
);
```

```SQL
ALTER TABLE `students`
ADD PRIMARY KEY (`id`);

ALTER TABLE `students`
MODIFY `id` int NOT NULL AUTO_INCREMENT;
```

```SQL
INSERT INTO `students` 
(`id`, `nameStud`, `rating`, `gender`, `date`, `city`) 
VALUES (NULL, 'Сидоров', '207', '1', '2002-08-03', 'Кунгур');
```

```SQL
INSERT INTO `students` 
(`nameStud`, `rating`, `gender`, `date`, `city`) 
VALUES ('Сидоров', '207', '1', '2002-08-03', 'Кунгур');
```

```SQL
INSERT INTO `students` (`nameStud`, `rating`, `gender`, `date`, `city`) VALUES
('Хомич', 207, 0, '2002-04-23', 'Кунгур'),
('Ежова', 212, 0, '2001-10-07', 'Лысьва');
```

```SQL
SELECT * FROM `students` WHERE `gender` = true
```

```SQL
UPDATE `students` SET `rating`=200 WHERE `nameStud`="Ежова";
```

```SQL
DELETE FROM `students` WHERE `rating` < 202;
```

```SQL
SELECT `nameStud`, `rating`, `city` FROM `students` ORDER BY `rating` DESC;
```

```SQL
SELECT `city`
FROM `students`
GROUP BY `city` 
ORDER BY `city` ASC;
```

```SQL
SELECT 
    `city`,
    COUNT(*) AS amount
FROM `students`
GROUP BY `city` 
ORDER BY `city` ASC;
```

```SQL
SELECT 
    `city`,
    COUNT(*) AS amount
FROM `students`
GROUP BY `city` 
ORDER BY `amount` DESC;
```

```SQL
SELECT 
    `date`,
    COUNT(*) AS amount 
FROM `students` 
GROUP BY `date` 
HAVING `amount` > 1;
```

```SQL
ALTER TABLE `groups` 
ADD FOREIGN KEY (`idCur`) 
REFERENCES `curators`(`id`) 
ON DELETE RESTRICT 
ON UPDATE RESTRICT;
```
