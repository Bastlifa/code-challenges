function sockMerchant(n, ar) {
    let sockObj = {}
    ar.forEach(el =>
    {
        if(sockObj[el]) sockObj[el] = sockObj[el] + 1
        else sockObj[el] = 1
    })

    let pairs = 0

    for(let s in sockObj)
    {
        pairs += Math.floor(sockObj[s]/2)
    }

    return pairs
}