# farmer, fox, chicken, grains
class State:
    BEGIN = False
    END = True
    def __init__(self, farmer: bool = False, fox: bool = False, chicken: bool = False, grains: bool = False):
        self.farmer = farmer
        self.fox = fox
        self.chicken = chicken
        self.grains = grains

    def get(self) -> tuple[bool, bool, bool, bool]:
        return (self.farmer, self.fox, self.chicken, self.grains)
    
    def isGoal(self) -> bool:
        values = [self.farmer, self.fox, self.chicken, self.grains]
        for i in values:
            if not i: return False
        return True
    
    def isValid(self) -> bool:
        if self.fox == self.chicken and self.fox != self.farmer:
            return False
        if self.chicken == self.grains and self.chicken != self.farmer:
            return False
        return True
    
    def __repr__(self) -> str:
        def convert(val: bool) -> str:
            return "END" if val else "BEGIN"
        farmer = convert(self.farmer)
        fox = convert(self.fox)
        chicken = convert(self.chicken)
        grains = convert(self.grains)
        return f'{farmer=} {fox=} {chicken=} {grains=}'

class Riddle:
    def __init__(self) -> None:
        self.state = State()
        self.history: list[tuple[bool, bool, bool, bool]] = []
        self.seen: set[tuple[bool, bool, bool, bool]] = set()
        self.history.append(self.state.get())
        self.seen.add(self.state.get())

    def nextStates(self) -> list[tuple[bool, bool, bool, bool]]:
        result: list[tuple[bool, bool, bool, bool]] = []
        farmer = self.state.farmer
        farmerNext = not farmer
        items = [self.state.fox, self.state.chicken, self.state.grains]
        result.append((farmerNext, items[0], items[1], items[2]))
        for i, v in enumerate(items):
            if v != farmer:
                continue
            itemsNext = [not itemVal if i == itemIndex else itemVal for itemIndex, itemVal in enumerate(items)]
            result.append((farmerNext, itemsNext[0], itemsNext[1], itemsNext[2]))
        return result
    
    def start(self) -> list[tuple[bool, bool, bool, bool]]:
        def search():
            nextStates = self.nextStates()
            for stateVal in nextStates:
                if stateVal in self.seen: continue
                state = State(*stateVal)
                if not state.isValid(): continue
                self.history.append(stateVal)
                self.seen.add(stateVal)
                if state.isGoal():
                    return self.history
                self.state = state
                result = search()
                if result: return result
                self.history.pop()
                self.seen.remove(stateVal)
        result = search()
        return result if result else []
    

if __name__ == '__main__':
    result = Riddle().start()
    for stateVal in result:
        state = State(*stateVal)
        print(state)



            
                