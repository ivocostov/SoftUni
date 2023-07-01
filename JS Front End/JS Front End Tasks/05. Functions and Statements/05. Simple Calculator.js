function simpleCalculator(num_1, num_2, operator) {
    validOperations = {
        'multiply': num_1 * num_2,
        'divide': num_1 / num_2,
        'add': num_1 + num_2,
        'subtract': num_1 - num_2
    }

    let result = validOperations[operator]

    console.log(result)
}


simpleCalculator(5, 5, 'multiply')
simpleCalculator(40, 8, 'divide')
simpleCalculator(12, 19, 'add')
simpleCalculator(50, 13, 'subtract')