// function palindromeIntegers(array) {

//     let isValid = true

//     for (let i = 0; i < array.length; i++) {
//         let numberAsString = array[i].toString()
        
//         if (numberAsString.length > 1) {
//             let numberAsStringHalfLenght = Math.floor(numberAsString.length / 2)
            
//             for (let numOfArray = 0; numOfArray < numberAsStringHalfLenght; numOfArray++) {
//             let firstDigit = Number(numberAsString[numOfArray])
//             let lastDigit = Number(numberAsString[numOfArray + numberAsString.length - 1 - numOfArray])
            
//                 if (firstDigit !== lastDigit) {
//                     isValid = false
//                     console.log(isValid)
//                     break
//                 } else if (numOfArray < numberAsStringHalfLenght - 1) {
//                     continue
//                 } else {
//                     isValid = true
//                     console.log(isValid)
//                 }
//             } 
//         } else {
//             isValid = true
//             console.log(isValid)
//             }
//     }
// }

// ***********************************************************************************************************************

function palindromeIntegers(array) {

    let isValid = true

    for (let i = 0; i < array.length; i++) {
        let numberAsString = array[i].toString()
        let numberAsStringReversed = numberAsString.split('').reverse().join('')

        if (numberAsString === numberAsStringReversed) {
            isValid = true
            console.log(isValid)
        } else {
            isValid = false
            console.log(isValid)
        }
    }
}


palindromeIntegers([123,323,421,121])
palindromeIntegers([32,2,232,1010])



