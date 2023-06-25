function evenAndOddSubtraction(array) {
    let even_sum = 0
    let odd_sum = 0

    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            even_sum += array[i]
        } else {
            odd_sum += array[i]
        }
    }
    console.log(even_sum - odd_sum)
}


evenAndOddSubtraction([1,2,3,4,5,6])
evenAndOddSubtraction([3,5,7,9])
evenAndOddSubtraction([2,4,6,8,10])