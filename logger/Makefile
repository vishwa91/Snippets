# Makefile to automate the compiling and moving it to the /usr/bin folder.

CC = gcc				
BINPATH = /usr/bin
# In case you want the installation to happen somewhere else, change BINPATH variable
SRC = log.c
DST = log
# Change this if you want to change the name of the program
SWITCH = -o
# Default switches, dont change unless you know what you are doing

all:
	$(CC) $(SWITCH) $(DST) $(SRC)
	mv $(DST) $(BINPATH)/$(DST)
clean:
	rm ./$(DST) 
