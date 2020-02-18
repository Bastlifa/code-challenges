let cache = {0: 0, 1: 1}

function fib(n, cache=null)
{
    if(n<2) return n
    else if(cache && cache[n] > 0) return cache[n]
    else
    {
        if(!cache)
        {
            cache = {}
            for(let i=0; i<n+1; i++)
            {
                cache[i] = 0
            }
        }
        cache[n] = fib(n-1, cache) + fib(n-2, cache)
        return cache[n]
    }
}

console.log(fib(6))