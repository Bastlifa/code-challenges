class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        
        def next_day(cell_state):
            temp = [0]*8
            for i in range(1, 7):
                temp[i] = int(cell_state[i-1] == cell_state[i+1])
            
            return temp
        
        i = N - 1
        cells = next_day(cells)
        
        states = []
        states.append(str(cells))
        repeat = False
        while i > 0 and not repeat:
            cells = next_day(cells)
            if str(cells) not in states:
                states.append(str(cells))
            else:
                repeat = True
            i -= 1
        
        x = (N - 1) % len(states)
        text = states[x][1:-1].split(', ')
        a = [int(t) for t in text]
        return a
    