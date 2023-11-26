# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directory alias
BIN_DIR:=bin
OBJ_DIR:=$(BIN_DIR)/.obj
CPP_DIR:=.
LEETCODE_NAME:=$(CPP_DIR)
UTIL_NAME:=$(CPP_DIR)/utils
INC_DIR:=$(CPP_DIR)/include
UTILS_INC_DIR=$(INC_DIR)/utils

# Compiler & flags
CC:=g++
# CFLAGS:=-O3 -s -std=c++20
CFLAGS:=-g -std=c++20

INCFLAGS:=-I$(INC_DIR) -I$(UTILS_INC_DIR)

UTIL_INCS:=$(wildcard $(UTILS_INC_DIR)/*.hpp)
# Get all cpp files in source
UTIL_SOURCES:=$(wildcard $(UTIL_NAME)/*.cpp)
LEETCODE_SOURCES:=$(wildcard $(LEETCODE_NAME)/*.cpp)
# Get all object files to compile later based on source files automatically
UTIL_OBJS:=$(patsubst $(UTIL_NAME)/%.cpp, $(OBJ_DIR)/$(UTIL_NAME)/%.o, $(UTIL_SOURCES))
LEETCODE_OBJS:=$(patsubst %.cpp, $(OBJ_DIR)/%.o, $(LEETCODE_SOURCES))
# Get all exe file names
LEETCODE_BINS:=$(patsubst $(OBJ_DIR)/$(LEETCODE_NAME)/%.o, $(BIN_DIR)/%, $(LEETCODE_OBJS))


## build: produce executable from source files
.PHONY: build
build: compile link

## compile: compile all source files to object files
.PHONY: compile
compile: $(UTIL_OBJS) $(LEETCODE_OBJS)
	
## link: link object files to executable
.PHONY: link
link: $(LEETCODE_BINS)

## check: detect source files
.PHONY: check
check:
	@echo "detecting c++ files ..."
	@echo "utils header files:\n" ${GREEN}$(UTIL_INCS)${NC}
	@echo "utils source files:\n" ${GREEN}$(UTIL_SOURCES)${NC}
	@echo "main source files:\n" ${GREEN}$(LEETCODE_SOURCES)${NC}
	@echo "util obj files to produce:\n" ${BLUE}$(UTIL_OBJS)${NC}
	@echo "main obj files to produce:\n" ${BLUE}$(LEETCODE_OBJS)${NC}
	@echo "binary files to produce:\n" ${BLUE}$(LEETCODE_BINS)${NC}

## clean: remove obj and exe dirs
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)

.PHONY: help
help: Makefile
	@sed -n 's/^##//p' $<

# Compile single cpp source file to object file
$(OBJ_DIR)/%.o: %.cpp $(UTIL_INCS)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(INCFLAGS) -o $@ -c $<

$(BIN_DIR)/%: $(UTIL_OBJS) $(OBJ_DIR)/$(LEETCODE_NAME)/%.o
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -o $@ $(OBJ_DIR)/$(LEETCODE_NAME)/$(@F).o $(UTIL_OBJS)
