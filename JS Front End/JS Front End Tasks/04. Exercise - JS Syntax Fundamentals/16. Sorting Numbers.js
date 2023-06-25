function sortingNumbers(arrayOfNumbers) {
    let newArrayOfNumbers = arrayOfNumbers.sort((a, b) => (a - b)) // Дава числата подредени във възходящ ред
    let newArray = []
    let length = arrayOfNumbers.length

    for (let i = 0; i < length; i++) {
        if (i % 2 === 0) {
            newArray.push(newArrayOfNumbers.shift())
        } else {
            newArray.push(newArrayOfNumbers.pop())
        }
    }

    return(newArray)
}

sortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56])