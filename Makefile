CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = editor

all: $(TARGET)

$(TARGET): editor.c
	$(CC) $(CFLAGS) -o $(TARGET) editor.c

clean:
	rm -f $(TARGET)

.PHONY: all clean
