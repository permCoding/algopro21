// Будем кодить тут: https://makecode.microbit.org/

input.onButtonPressed(Button.A, () => 
    basic.showIcon(IconNames.Yes)
);

let cls = () => basic.clearScreen();

input.onButtonPressed(Button.B, cls);
