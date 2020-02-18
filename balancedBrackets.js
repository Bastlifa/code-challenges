function balancedBrackets(str) {
    let line = str.split('')
    const stack = []
    let ans = true;
    let openPipe = true
    const open = {'(': ')', '{': '}', '[': ']', '|': '|'}
    const close = {')': true, '}': true, ']': true, '|': true}
    line.forEach(item => {
        if (open[item] && (item !== '|' || openPipe === true))
        {
            stack.push(item);
            if(item == '|') openPipe = false
        } else if (close[item] && (item !== '|' || openPipe === false))
        {
            if (open[stack.pop()] !== item) ans = false;
            if(item == '|') openPipe = true
        }
    });
    return ans && stack.length === 0;
}

