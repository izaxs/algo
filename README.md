# Prerequisite

C++ compiler that supports C++17

VSCode with C/C++ extension is recommended for debugging

## Linux Debian
```bash
sudo apt update
sudo apt install build-essential gdb
```

## Mac OS
```bash
xcode-select --install
```
Install CodeLLDB in VSCode

# How to Code
## LeetCode

Add solution c++ file as ```leetcode/[0-9]{4}.cpp```

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

Take Leetcode #1 as example:
```bash
make
bin/0001
```

# Debug in VSCode
## GDB
Select "GDB: Debug leetcode active file" in debug options

## LLDB
Select "LLDB: Debug leetcode active file" in debug options

# Other Commands
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
