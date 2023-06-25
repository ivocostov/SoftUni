function mathOperations (num_1, num_2, operand) {
    let result = 0

    switch (operand) {
        case '+': result = num_1 + num_2; break;
        case '-': result = num_1 - num_2; break;
        case '*': result = num_1 * num_2; break;
        case '/': result = num_1 / num_2; break;
        case '%': result = num_1 % num_2; break;
        case '**': result = num_1 ** num_2; break;
    }

    console.log(result)
}

mathOperations(5, 6, '+')
mathOperations(3, 5.5, '*')