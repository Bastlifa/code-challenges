function numberOfWays(queries) {
    // Write your code here

    // make a function to count each query
    function countThem(query)
    {
        let aMax = Math.min(query[0], query[1])
        let b = Math.max(query[0], query[1])

        let count = 0

        for(let i=1; i<=aMax; i++)
        {
            count += (aMax + 1 - i)*(b + 1 - i)
        }

        return count
    }

    let retArr = []

    queries.forEach(el => retArr.push(countThem(el)))

    return retArr
}