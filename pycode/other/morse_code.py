# Let's write a function that translates from the raw signal (1's and 0's) to the
# intermediate representation of morse code

# signal = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]

# A "." is one or two 1's in a row (1 or 1,1)
# A "-" is three, four or five 1's in a row (1,1,1 or 1,1,1,1 or 1,1,1,1,1)
# A short pause (represented as the empty string "" in the output) is one or two 0's in a row (0 or 0,0)
# A long pause (represented as a " " in the output) is 3, 4, or 5 0's in a row

# You should create a function parse_morse() that will return the string "... --.-" 
# Ex: assert "... --.-" == parse_morse(signal)

morse_table = { 
    ".-":     "a",
    "-...":   "b",
    "-.-.":   "c",
    "-..":    "d",
    ".":      "e",
    "..-.":   "f",
    "--.":    "g",
    "....":   "h",
    "..":     "i",
    ".---":   "j",
    "-.-":    "k",
    ".-..":   "l",
    "--":     "m",
    "-.":     "n",
    "---":    "o",
    ".--.":   "p",
    "--.-":   "q",
    ".-.":    "r",
    "...":    "s",
    "-":      "t",
    "..-":    "u",
    "...-":   "v",
    ".--":    "w",
    "-..-":   "x",
    "-.--":   "y",
    "--..":   "z",
}


def parse_morse(signal: list[int]) -> str:
    def extract(pos: int) -> tuple[str, int]:
        if pos >= len(signal): return '', pos
        cur, i = signal[pos], pos + 1
        while i < len(signal) and signal[i] == cur and i - pos <= 5:
            i += 1
        signalLen = i - pos
        if cur == 1:
            if signalLen <= 2: return '.', i
            return '-', i
        else:
            if signalLen <= 2: return '', i
            return ' ', i
    cursor = 0
    results: list[str] = []
    while cursor < len(signal):
        morse, cursor = extract(cursor)
        results.append(morse)
    return ''.join(results)

# Now we want to parse actual strings (e.g. "square").

# We'll go ahead and add words, which are separated by 6 or more 0's. For example:

# signal =  [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0]


# assert "join square" == decode_morse(signal)


def parse_morse2(signal: list[int]) -> str:
    def extract(pos: int) -> tuple[str, int]:
        if pos >= len(signal): return '', pos
        cur, i = signal[pos], pos + 1
        while i < len(signal) and signal[i] == cur:
            if (cur == 1 and i - pos <= 5) or cur == 0:
                i += 1
        signalLen = i - pos
        if cur == 1:
            if signalLen <= 2: return '.', i
            return '-', i
        else:
            if signalLen <= 2: return '', i
            if signalLen >= 6: return '@', i
            return ' ', i
    cursor = 0
    results: list[str] = []
    while cursor < len(signal):
        morse, cursor = extract(cursor)
        results.append(morse)
    return ''.join(results)

def decode_morse(signal: list[int]) -> str:
    morse_dashes = parse_morse2(signal)
    def extract(pos: int) -> tuple[str, int]:
        if pos >= len(morse_dashes): return '', pos
        if morse_dashes[pos] == '@': return ' ', pos + 1
        if morse_dashes[pos] == ' ': return '', pos + 1
        i = pos
        while i < len(morse_dashes) and morse_dashes[i] != ' ' and morse_dashes[i] != '@':
            i += 1
        return morse_dashes[pos:i], i
    cursor = 0
    result: list[str] = []
    while cursor < len(morse_dashes):
        code, cursor = extract(cursor)
        if code == '': continue
        elif code == ' ': result.append(' ')
        else: result.append(morse_table[code])
    return ''.join(result)

if __name__ == '__main__':
    # signal = [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
    # morseCode = parse_morse(signal)
    # print(morseCode)

    signal = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0]
    words = decode_morse(signal)
    print(words)
        