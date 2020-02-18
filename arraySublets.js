function subsetA(arr) {
    // Write your code here
    if(arr.length === 0) return arr

    arr = arr.sort((a,b) => b-a)
    let a = []
    let sumArr = arr.reduce((acc, cur) => acc += cur)
    let sumA = 0
    while(sumA <= sumArr && arr.length > 0 && arr[0] > 0)
    {
        a.unshift(arr[0])
        sumA += arr[0]
        sumArr -= arr[0]
        arr.shift()
    }
    return a
}