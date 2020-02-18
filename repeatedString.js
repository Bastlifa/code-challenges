function repeatedString(s, n) {
    if(s === "") return 0
    let aCount = 0
    let charCount = 0
    const sLength = s.length
    let aInS = 0
    for(let i=0; i<s.length; i++)
    {
        if(s[i] === 'a') aInS++
    }

    aCount += Math.floor(n/sLength)*aInS

    for(let i=0; i<n%sLength; i++)
    {
        if(s[i] === 'a') aCount++
    }

    return aCount
}