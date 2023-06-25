function printAndSum(startNum, endNum) {
    let numbers = []
    let sum = 0
    for (let i = startNum; i <= endNum; i++) {
        numbers.push(i)
        sum += i;
    }

    console.log(numbers.join(' '))
    console.log(`Sum: ${sum}`)
}

printAndSum(5, 10)
printAndSum(0, 26)