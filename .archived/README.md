## Archived Language Solutions

Find them in ```/.archived```

### Choose Language
Go: 1.16+

C++: Compiler that supports C++17

### Editor
VSCode with ```[Go | C/C++]``` extension is recommended for debugging

### Linux Debian
```bash
sudo apt update
sudo apt install build-essential gdb
```

### Mac OS
```bash
xcode-select --install
```
Install CodeLLDB in VSCode

## How to Code
### Archived Go Solutions
Add Go solution file as ```.archived/gocode/h??/[0-9]{4}.go```

Note that ```h??``` means grouping every one hundred solutions into a diretory

For example, the path of solution #1234 should be ```.archived/gocode/h12/1234.go```

### Archived C++ Solutions
Add C++ solution file as ```.archived/pluscode/[0-9]{4}.cpp```

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

## Build & Run
### Go
Run the classic test command for each Go test file, eg.

```go test -timeout 30s -run ^Test_twoSum$ github.com/gearbird/algo/h00 ```

However, if VSCode Go extension is installed, clicking ```"run test"``` or ```"debug test'``` button above the test functions would be much easier

### C++
Take Leetcode #1 as example:
```bash
make
bin/0001
```

### Debug C++ in VSCode
### GDB
Select "GDB: Debug leetcode active file" in debug options

### LLDB
Select "LLDB: Debug leetcode active file" in debug options

### Other Commands for C++
### Call help for Makefile
```bash
make help
```

#### Check all project related files in project
```bash
make check
```

#### Clean up binary files
```bash
make clean
```
