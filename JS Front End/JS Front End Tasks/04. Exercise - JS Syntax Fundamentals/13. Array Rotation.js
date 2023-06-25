"use strict";

function arrayRotation(array, rotationCycles) {
    
    let newArray = array

    for (let i = 0; i < rotationCycles; i++) {
        let firstElement = newArray.shift();
        newArray.push(firstElement)
    }

    console.log(newArray.join(' '))
    
}

arrayRotation([51, 47, 32, 61, 21], 2)
arrayRotation([32, 21, 61, 1], 4)
