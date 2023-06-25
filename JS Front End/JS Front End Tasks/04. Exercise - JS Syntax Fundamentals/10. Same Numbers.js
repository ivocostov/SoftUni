"use strict";


function sameNumbers(number) {
    let numbersArray = Array.from(number.toString(), Number) // Създаване на array от числата като стринг и след това отново преобразувани на числа, 
    const numbersSet = new Set(numbersArray)                 // защото числата не могат да се обхождат. След което array се поставя в Set.
    let isTrue = true

    if (numbersSet.size !== 1) {
        isTrue = false
    }
// Смятане на сбора на числата
    const sum = numbersArray.reduce((currentNumber, nextNumber) => {return currentNumber + nextNumber}, 0)
    
    console.log(isTrue)
    console.log(sum)
}

sameNumbers(2222222)
sameNumbers(1234)