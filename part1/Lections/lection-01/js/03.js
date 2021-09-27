// npm i readline-sync
readln = require('readline-sync'); // подключаем модуль
modend = require('./module-node'); // подключаем модуль

console.log("Введите радиус");
radius = +readln.question(); // читаем с консоли
console.log("Введите количество знаков после запятой"); 
count = +readln.question(); // читаем с консоли

console.log("Площадь круга = ", modend.squareCircle(radius, count));
