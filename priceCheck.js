function priceCheck(products, productPrices, productSold, soldPrice) {
    // Write your code here
    let priceObj = {}

    products.forEach((el, index) =>
    {
        priceObj[el] = productPrices[index]
    })

    let errors = 0
    productSold.forEach((el, index) =>
    {
        if(priceObj[el] !== soldPrice[index]) errors++
    })

    return errors
}