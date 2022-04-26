-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Апр 03 2021 г., 17:28
-- Версия сервера: 8.0.22-0ubuntu0.20.04.2
-- Версия PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `soft0015_faculty`
--

-- --------------------------------------------------------

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
