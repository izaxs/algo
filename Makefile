# Directory alias
SRC_DIR=src
INC_DIR=inc
OBJ_DIR=obj
BIN_DIR=bin

# Compiler & flags
CC=g++
CFLAGS=-I$(INC_DIR) -g

# Get all cpp files in source
ALL_SOURCES=$(wildcard $(SRC_DIR)/*.cpp)
# Get all object files to compile later based on source files automatically
ALL_OBJS=$(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(ALL_SOURCES))

LINK_TARGET_MAIN=$(BIN_DIR)/main

## build: produce executable from source files
.PHONY: build
build: prepare compile link

## run: execute main
.PHONY: run
run: prepare $(LINK_TARGET_MAIN)
	@echo
	@./$(LINK_TARGET_MAIN)
	@echo

## prepare: make sure dirs are in place
.PHONY: prepare
prepare:
	@mkdir -p $(BIN_DIR) $(OBJ_DIR)

## compile: compile all source files to object files
.PHONY: compile
compile: $(ALL_OBJS)
	
## link: link object files to executable
.PHONY: link
link: $(LINK_TARGET_MAIN)

## clean: remove obj and exe dirs
.PHONY: clean
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<

# Compile single cpp source file to object file
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CC) $(CFLAGS) -o $@ -c $<

$(LINK_TARGET_MAIN): $(ALL_OBJS)
	$(CC) $(CFLAGS) -o $(LINK_TARGET_MAIN) $(ALL_OBJS)