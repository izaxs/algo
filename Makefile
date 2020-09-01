SRC_DIR=src
INC_DIR=inc
OBJ_DIR=obj
BIN_DIR=bin

ALL_SOURCE_FILES=$(wildcard $(SRC_DIR)/*.cpp)
ENTRY_FILE=main.cpp

BIN_FILE=main

CC=g++
CFLAGS=-I$(INC_DIR) -g

.PHONY: build
build: $(BIN_DIR) $(BIN_DIR)/$(BIN_FILE)

.PHONY: clean
clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

$(BIN_DIR)/$(BIN_FILE): $(ALL_SOURCE_FILES)
	$(CC) $(CFLAGS) -o $(BIN_DIR)/$(BIN_FILE) $(SRC_DIR)/$(ENTRY_FILE)

