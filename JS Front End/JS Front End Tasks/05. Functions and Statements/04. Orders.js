function orders(product, productQuantity) {
    productsDict = {
        'coffee': 1.50,
        'water': 1.00,
        'coke': 1.40,
        'snacks': 2.00,
    }

    let totalSum = productsDict[product] * productQuantity
    console.log(totalSum.toFixed(2))
}

orders("water", 5)
orders("coffee", 2)