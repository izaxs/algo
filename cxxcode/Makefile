# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# CPP_VERSION:=c++17
CPP_VERSION:=c++20

# Directory alias
PROJ_DIR:=$(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
INC_DIR:=$(PROJ_DIR)/inc
SRC_DIR:=$(PROJ_DIR)/src
BIN_DIR:=$(PROJ_DIR)/bin
OBJ_DIR:=$(BIN_DIR)/.obj

UTILS_NAME:=utils
INC_UTILS_DIR=$(INC_DIR)/$(UTILS_NAME)
SRC_UTILS_DIR:=$(SRC_DIR)/$(UTILS_NAME)
OBJ_UTILS_DIR:=$(OBJ_DIR)/$(UTILS_NAME)

# Compiler & flags
CC:=g++
# CC_FLAGS:=-O3 -s -std=$(CPP_VERSION)
CC_FLAGS:=-g -std=$(CPP_VERSION)

INC_FLAGS:=-I$(INC_DIR) -I$(INC_UTILS_DIR)
# Names for all utils header files
INC_UTILS_HPP:=$(wildcard $(INC_UTILS_DIR)/*.hpp)
# Names for all source files
SRC_MAIN_CPP:=$(wildcard $(SRC_DIR)/*.cpp)
SRC_UTILS_CPP:=$(wildcard $(SRC_UTILS_DIR)/*.cpp)
# Names for all object files
OBJ_MAIN:=$(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRC_MAIN_CPP))
OBJ_UTILS:=$(patsubst $(SRC_UTILS_DIR)/%.cpp, $(OBJ_UTILS_DIR)/%.o, $(SRC_UTILS_CPP))
# Names for all main exe files
BIN_MAIN:=$(patsubst $(OBJ_DIR)/%.o, $(BIN_DIR)/%, $(OBJ_MAIN))

## build: produce executable from source files
.PHONY: build
build: compile link

## compile: compile all source files to object files
.PHONY: compile
compile: $(OBJ_MAIN) $(OBJ_UTILS)
	
## link: link object files to executable
.PHONY: link
link: $(BIN_MAIN)

## check: detect source files
.PHONY: check
check:
	@echo "detecting c++ files ..."
	@echo "utils header files:\n" ${GREEN}$(INC_UTILS_HPP)${NC}
	@echo "utils source files:\n" ${GREEN}$(SRC_UTILS_CPP)${NC}
	@echo "main source files:\n" ${GREEN}$(SRC_MAIN_CPP)${NC}
	@echo "util obj files to produce:\n" ${BLUE}$(OBJ_UTILS)${NC}
	@echo "main obj files to produce:\n" ${BLUE}$(OBJ_MAIN)${NC}
	@echo "binary files to produce:\n" ${BLUE}$(BIN_MAIN)${NC}

## clean: remove obj and exe dirs
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)

.PHONY: help
help: Makefile
	@sed -n 's/^##//p' $<

# Compile single cpp source file to object file
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp $(INC_DIR)
	@mkdir -p $(@D)
	$(CC) $(CC_FLAGS) $(INC_FLAGS) -o $@ -c $<

$(BIN_DIR)/%: $(OBJ_DIR)/%.o $(OBJ_UTILS) 
	@mkdir -p $(@D)
	$(CC) $(CC_FLAGS) -o $@ $(OBJ_DIR)/$(@F).o $(OBJ_UTILS)
