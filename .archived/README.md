## Archived Language Solutions

Find them in ```/.archived```

### Choose Language
C#: .NET 6

TypeScript: 4.6+

Python: Python 3.9+

Go: 1.16+

C++: Compiler that supports C++17

### Editor
VSCode with ```[Deno | Python | Go | C/C++]``` extension is recommended for debugging

### Linux Debian
Deno:

```
cargo install deno --locked
```

Python:

```bash
sudo apt update
sudo apt install python
```

C++:

```bash
sudo apt update
sudo apt install build-essential gdb
```

### Mac OS
Deno:

```
brew install deno
```

Python:

```bash
xcode-select --install
brew install python
```

C++:

```bash
xcode-select --install
```
Install CodeLLDB in VSCode

## How to Code
### Archived C# Solutions
Find the solutions and tests in ```.archived/sharpcode```

Solutions are located in the buckets with prefix ```Hxx```, x is the prefix for every 100 solutions, for example, solution 1999 is located at bucket H19

### Archived TypeScript Solutions
TODO

### Archived Python Solutions
Add Python solution file as ```.archived/snakecode/[0-9]{4}.py```

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
