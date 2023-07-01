function signCheck(numOne, numTwo, numThree) {
    let result = numOne * numTwo * numThree

    if (result < 0) {
        console.log('Negative')
    } else {
        console.log('Positive')
    }
}

signCheck(5, 12, -15)
signCheck(-6, -12, 14)
signCheck(-1, -2, -3)
