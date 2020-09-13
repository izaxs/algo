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

# How to Code
## LeetCode

Add solution c++ file under ```leetcode/solution/*```

Declare test function in ```leetcode/list.hpp```

Call test function in ```leetcode/main.cpp```

# Build & Run

```bash
make run
```

# Debug in VSCode

## GDB
Select "GDB: Debug leetcode" in debug options

## LLDB
Install CodeLLDB

Select "LLDB: Debug leetcode" in debug options

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
