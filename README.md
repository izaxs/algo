## Why choose Python for Coding Interview

1. Python is less verbose, compared to Java
2. Python standard library includes the necessary builtin algorithms and data structures like sort, heap... compared to JavaScript or Go (Generic is coming though)
3. Python is easy to debug, all you need is to open a file, then VSCode extensions does the magic, compared to Java or C++
4. Python is widely used and popular in coding interview, compared to C# or GO or Rust
5. Type Annotation is matured since Python 3.9, strict static analysis is provided by Pylance, it's a bit eaiser to locate bugs

## LeetCode Python Solutions

Find them in ```/snakecode```

## Other Archived Language Solutions

Find them in ```/.archived```

## Language Prerequisite

Python: Python 3.9+

### Archived Solution Languages
Go: 1.16+

C++: Compiler that supports C++17

### Editor
VSCode with ```[Go | Python | C/C++]``` extension is recommended for debugging

### Linux Debian
```bash
sudo apt update
sudo apt install build-essential gdb
sudo apt install python
```

### Mac OS
```bash
xcode-select --install
brew install python
```
Install CodeLLDB in VSCode

## How to Code
### LeetCode Python Solutions
Add Python solution file as ```snakecode/[0-9]{4}.py```

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
### Python
Just F5 run active Python files in snakecode

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
