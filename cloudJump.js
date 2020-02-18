function jumpingOnClouds(c) {
    let curCloud = 0
    let jumps = 0
    while(curCloud !== c.length - 1)
    {
        if(curCloud < c.length - 1 && c[curCloud +2] == 0)
        {
            curCloud += 2
            jumps +=1
        }
        else
        {
            curCloud += 1
            jumps += 1
        }
    }
    return jumps
}