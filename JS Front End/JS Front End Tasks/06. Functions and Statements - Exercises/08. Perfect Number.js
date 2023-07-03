function perfectNumber(number) {
    let sumOfDivisors = 0
    
    for (let i = 1; i < number; i++) {
        if (number % i === 0) {
            sumOfDivisors += i
        }
    }

    if (sumOfDivisors === number) {
        console.log("We have a perfect number!")
    } else {
        console.log("It's not so perfect.")
    }
}

perfectNumber(6)
perfectNumber(28)
perfectNumber(1236498)
