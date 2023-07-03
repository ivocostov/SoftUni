function oddAndEvenSum(number) {
    let numberAsString = number.toString()
    let oddSum  = 0
    let evenSum  = 0

    for (let i = 0; i < numberAsString.length; i++) {
        if (Number(numberAsString[i]) % 2 === 0) {
            evenSum += Number(numberAsString[i])
        } else {
            oddSum += Number(numberAsString[i])
        }
        
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

oddAndEvenSum(1000435)
oddAndEvenSum(3495892137259234)