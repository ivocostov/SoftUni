function sumDigits(number) {
    let digitsAsString = (number).toString()
    let sum = 0

    for (let i = 0; i < digitsAsString.length; i++) {
        sum += Number(digitsAsString[i]);
    }

    console.log(sum)
}

sumDigits(245678)
sumDigits(97561)
sumDigits(543)