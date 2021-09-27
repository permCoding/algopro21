// Будем кодить тут: https://makecode.microbit.org/

let num = 0;

basic.showNumber(num);

input.onButtonPressed(Button.A, () => {
    num -= 1;
    basic.showNumber(num);
});

input.onButtonPressed(Button.B, () => {
    num++;
    basic.showNumber(num);
});
