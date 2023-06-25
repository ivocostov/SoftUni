function reverseAnArrayOfNumbers(number, array) {
    let new_array = []

    for (let i = 0; i < number; i++) {
        new_array.push(array[i])
    }
    console.log( new_array.reverse().join(' '))
}

reverseAnArrayOfNumbers(3, [10, 20, 30, 40, 50])
reverseAnArrayOfNumbers(4, [-1, 20, 99, 5])
reverseAnArrayOfNumbers(2, [66, 43, 75, 89, 47])