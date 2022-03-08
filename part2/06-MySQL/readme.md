## MySQL  

---  

MySQL doc  
https://dev.mysql.com/doc/refman/8.0/en/select-into.html  

```  

```  

---  

### examples  

```
CREATE TABLE `soft0015`.`curators` ( `id` INT NOT NULL AUTO_INCREMENT , `nameCur` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
```

```
CREATE TABLE IF NOT EXISTS `soft0015`.`TABLE 2` (`id` int(1), `nameCur` varchar(7)) DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```

```
создать индекс
"ALTER TABLE `groups` ADD INDEX(`idCur`);"

DROP TABLE `soft0015`.`curators`
```

```
CREATE TABLE `soft0016_faculty`.`groups` ( `id` INT NOT NULL AUTO_INCREMENT , `nameGr` VARCHAR(20) NOT NULL , `idCur` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
```

```
SELECT `groups`.`nameGr`, `curators`.`nameCur` 
FROM `groups`,`curators` 
WHERE `groups`.`idCur`=`curators`.`id`
```

```
SELECT `groups`.`nameGr`, `curators`.`nameCur` 
FROM `groups` JOIN `curators` 
ON `groups`.`idCur`=`curators`.`id`
LIMIT 2
```

```
CREATE TABLE `soft0016_faculty`.`students` 
(`id` INT NOT NULL AUTO_INCREMENT, 
`nameSt` VARCHAR(20) NOT NULL, 
`sex` INT NOT NULL, 
`age` INT NOT NULL, 
`idGr` INT NOT NULL, 
PRIMARY KEY (`id`)) 
ENGINE = InnoDB;
```

```

```


```
-- так можно оформить однострочный коммент
--
-- Структура таблицы `curators`
--

CREATE TABLE `curators` (
  `id` int NOT NULL,
  `nameCur` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `curators`
--

INSERT INTO `curators` (`id`, `nameCur`) VALUES
(1, 'Мухин'),
(2, 'Ухова'),
(3, 'Ухова'),
(4, 'Ляскин'),
(5, 'Дуров'),
(6, 'Нектов'),
(7, 'Ктотов'),
(8, 'ЕщёОдин'),
(9, 'Второй');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `curators`
--
ALTER TABLE `curators`
  ADD PRIMARY KEY (`id`);
COMMIT;
```

```
ALTER TABLE `groups` ADD FOREIGN KEY (`idCur`) 
REFERENCES `curators`(`id`) 
ON DELETE RESTRICT ON UPDATE RESTRICT;
```

