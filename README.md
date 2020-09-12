# Prerequisite

C++ compiler that supports C++17

Linux Debian:
```bash
sudo apt update
sudo apt install build-essential gdb
```

Mac OS:
```bash
xcode-select --install
```

# Build & Run

```bash
make run
```

# Debug

## Use GDB in VSCode:
Select "GDB: Debug leetcode" in debug options

## Use LLDB in VSCode:
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
