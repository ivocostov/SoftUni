function nXnMatrix(size) {
    // let matrix = Array(size).fill(Array(size))

    let matrixRow = ''

    for (let i = 0; i < size; i++) {
        matrixRow += `${size} `
    }

    for (let j = 0; j < size; j++) {
        console.log(matrixRow)
    }
}

nXnMatrix(3)
nXnMatrix(7)
nXnMatrix(2)