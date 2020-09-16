# Prerequisite

C++ compiler that supports C++17

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

Add solution c++ file under ```leetcode/solution/*```

Declare test function in ```leetcode/list.hpp```

Call test function in ```leetcode/main.cpp```

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
## Build project only
```bash
make build
```

## Check all header and source files in project
```bash
make check
```

## Clean up binary files
```bash
make clean
```
