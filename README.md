# Prerequisite
## Based on the language of choice:

Go: 1.16+

Python: Python 3.7+

C++: Compiler that supports C++17

VSCode with ```[Go | Python | C/C++]``` extension is recommended for debugging

## Linux Debian
```bash
sudo apt update
sudo apt install build-essential gdb
sudo apt install python
```

## Mac OS
```bash
xcode-select --install
brew install python
```
Install CodeLLDB in VSCode

# How to Code
## LeetCode
### Go Solutions
Add Go solution file as ```gocode/h??/[0-9]{4}.go```

Note that ```h??``` means grouping every one hundred solutions into a diretory

For example, the path of solution #1234 should be ```gocode/h12/1234.go```

### Python Solutions
Add Python solution file as ```snakecode/[0-9]{4}.py```

### C++ Solutions
Add C++ solution file as ```pluscode/[0-9]{4}.cpp```

Boilerplate code:
```cpp
#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    // solution
}

int main() {
    using namespace leetcode;
    // test code
}
```

# Build & Run
### Go
Run the classic test command for each Go test file, eg.

```go test -timeout 30s -run ^Test_twoSum$ github.com/gearbird/algo/gocode/00xx ```

However, if VSCode Go extension is installed, clicking ```"run test"``` or ```"debug test'``` button above the test functions would be much easier

### Python
Just run Python file in snakecode

### C++
Take Leetcode #1 as example:
```bash
make
bin/0001
```

# Debug C++ in VSCode
## GDB
Select "GDB: Debug leetcode active file" in debug options

## LLDB
Select "LLDB: Debug leetcode active file" in debug options

# Other Commands for C++
## Call help for Makefile
```bash
make help
```

## Check all project related files in project
```bash
make check
```

## Clean up binary files
```bash
make clean
```
