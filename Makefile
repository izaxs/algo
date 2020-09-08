# Directory alias
OBJ_DIR:=obj
BIN_DIR:=bin
LEETCODE_SRC_DIR:=leetcode
LEETCODE_INC_DIR:=$(LEETCODE_SRC_DIR)/include

# Compiler & flags
CC:=g++
# CFLAGS:=-O3 -s -std=c++17
CFLAGS:=-g -std=c++17

ALL_INCS:=$(wildcard $(LEETCODE_INC_DIR)/*.hpp) $(wildcard $(LEETCODE_INC_DIR)/**/*.hpp)
# Get all cpp files in source
ALL_SOURCES:=$(wildcard $(LEETCODE_SRC_DIR)/*.cpp) $(wildcard $(LEETCODE_SRC_DIR)/**/*.cpp)
# Get all object files to compile later based on source files automatically
ALL_OBJS:=$(patsubst %.cpp, $(OBJ_DIR)/%.o, $(ALL_SOURCES))

LEETCODE_LINK_TARGET:=$(BIN_DIR)/leetcode

## build: produce executable from source files
.PHONY: build
build: compile link

## run: execute main
.PHONY: run
run: $(LEETCODE_LINK_TARGET)
	@echo
	@./$(LEETCODE_LINK_TARGET)
	@echo

## compile: compile all source files to object files
.PHONY: compile
compile: $(ALL_OBJS)
	
## link: link object files to executable
.PHONY: link
link: $(LEETCODE_LINK_TARGET)

## check: detect source files
.PHONY: check
check:
	@echo "detecting c++ files ..."
	@echo "header files:" $(ALL_INCS)
	@echo "source files:" $(ALL_SOURCES)

## clean: remove obj and exe dirs
.PHONY: clean
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<

# Compile single cpp source file to object file
$(OBJ_DIR)/%.o: %.cpp $(ALL_INCS)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -o $@ -c $<

$(LEETCODE_LINK_TARGET): $(ALL_OBJS)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $(LEETCODE_LINK_TARGET) $(ALL_OBJS)
