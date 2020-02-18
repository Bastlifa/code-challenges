function countingValleys(n, s) {
    let valleys = 0
    let inValley = false
    let inMountain = false
    let elevation = 0

    for(let i=0; i<s.length; i++)
    {
        if(s[i] === 'U')
        {
            elevation += 1
            if(inMountain === false && elevation > 0)
            {
                inMountain = true
            }
            else if(inValley === true && elevation === 0)
            {
                valleys += 1
                inValley = false
            }
        }
        else if(s[i] === 'D')
        {
            elevation -= 1
            if(inMountain === true && elevation === 0)
            {
                inMountain = false
            }
            else if(inValley === false && elevation < 0)
            {
                inValley = true
            }
        }
    }

    return valleys

}