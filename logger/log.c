/*
* Author:		Vishwanath
* Email:		<vishwa.hyd@gmail.com>
* Dependencies:	None
* 
* Simple program to log your daily comments in a file.
* The logging file will change every month, so that 
* logging does not get cluttered
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#include<unistd.h>

#define MAXPATH	256
#define MAXLEN 32
#define MAXMSG 1024

char *getTime( void )			// Function to directly get the time in string format
{
	time_t raw_time;			// raw_time holds time from 00:00 Jan 1 1970
	struct tm * timeinfo;		// This variable holds local time
	char *timestring;			// Output string pointer
	
	time(&raw_time);
	timeinfo = localtime(&raw_time);
	
	timestring = asctime(timeinfo);	// Convert the time into a string
	
	return timestring;
}

/*
* To check if a file exists, we will use access(filename, F_OK)
* This will return -1 if the file doesnot exist.
* F_OK is to confirm the file existence. Other switches are:
* R_OK: read permission
* W_OK: write permission
* X_OK: execute permission
* 
* To check if a folder exits,
* struct stat st;
* if( stat(folderpath, &st) == 0)
* 	printf("folder exists");
* 
*/

/*
* When using strcpy, make sure that destination pointer 
* is already allocated memory, otherwise, it gives a 
* segmentation fault. 
* Also, segmentation fault occurs if a file opening fails,
* or you open the file in read mode and instead, write to it.
*
*/
int log_init( char * filename )				// This function will initialise the logging file
{
	char * time;							// Will hold the present time
	char * pwd;								// Will hold the present working directory
	char * delims = " \n";
	
	char time_split[5][MAXLEN];
	char *temp;
	char *word;
	
	int i = 0;
	
	if( access(filename, F_OK) == 0 )
	{
		printf("File with the given name already exits. Cannot create\n");
		exit(1);
	}
	
	pwd = getenv("PWD");
	strcat(pwd, "/");
	strcat(pwd, filename);
	
	time = getTime();
	temp = NULL;							// Split the time fields so that we can use the date 
	temp = strtok(time, delims);
	
	strcpy(time_split[i++], temp);
	
	while ( i < 5 )
	{
		word = strtok(NULL, delims);
		strcpy(time_split[i++], word);
	} 
	strcat(pwd, "_");						// Append the month to change the log every month
	strcat(pwd, time_split[1]);
	
	FILE *fp = fopen(pwd, "wb");			// Now open the file
	time = getTime();						// Refresh time. This is done, since strtok is corrupting it
	
	char *_username;						// An important step, we should not meddle with the getenv output,
	char username[MAXPATH];					// which would give undesirable results
	_username = getenv("USER");
	strcpy(username, _username);
	strcat(username,"/.logfile");
	
	char tempath[strlen(username)];	
	strcpy(tempath, username);
	strcpy(username, "/home/");
	strcat(username, tempath);
	FILE *info = fopen(username, "wb");		// This file will hold the path to the logging
											// file and the present month
	printf("Created log file ");
	puts(pwd); 
	printf("log file created on %s", time);
	//puts(time);
	
	fprintf(fp, "log file created on %s",time);						// Write the time to the log file
	fprintf(fp, "*********************************************\n");
	fputs(pwd, info);												// info file will have the path to the logging	
	fputs("\n", info);												// file and the month last in which it was logged
	fputs(time_split[1], info);
	fclose(fp);
	fclose(info);
	
}
int writeLog(char *message)		// This function will write the log to the logging file
{
	FILE *fp;
	FILE *info;
	
	char path[MAXPATH];			
	char month[MAXLEN];			
	char *delims = " \n";
	
	char *time;
	char time_split[5][MAXLEN];
	char *temp;
	
	char userpath[MAXPATH];
	char *username;
	char home[MAXPATH];
	
	username = getenv("USER");		// DONOT meddle with the getenv value. Everything will go bonkers
	strcpy(userpath, username);
	strcpy(home, userpath);
	strcpy(userpath, "/home/");		// Create the absolute path of the logging and the info file
	strcat(userpath, home);
	strcat(userpath, "/.logfile");
	info = fopen(userpath, "rb");	
	int i = 0;
	
	time = getTime();				// retrieve present time. Only used for month
	
	temp = NULL;					// Split the time fields so that we can use the date 
	temp = strtok(time, delims);
	
	strcpy(time_split[i++], temp);
	while (i < 5)
	{
		temp = strtok(NULL, delims);
		strcpy(time_split[i++], temp);
	}
	
	fgets(path, MAXPATH, info);		// Retrieve the absolute path of the logging file
	fgets(month, MAXPATH, info);	// Retrieve the last logged month
	
	i = strlen(path);
	path[i-1] = '\0';				// Remove the \n at the end of the path descriptor
	
	if (strcmp(month, time_split[1]) == 0);	// If the months match, do nothing
	else									// Else, start a new file with _{new month}
	{
		while(path[i--] != '_');
		path[i+2] = '\0';
		strcat(path, time_split[1]);
		fclose(info);
		
		char *user;
		char garb[MAXLEN];
		user = getenv("USER");
		
		strcpy(garb, user);
		strcpy(user, "/home/");
		strcat(user, garb);		
		strcat(user, "/.logfile");
		FILE *info = fopen(user, "wb");
		fputs(path, info);
		fputs("\n", info);
		fputs(time_split[1], info);
		fclose(info);
	};	
	
	time = getTime();				// This time will be the time stamp
	fp = fopen(path, "a");			// Now open the file and append the timestamp and message
	fprintf(fp, "Time stamp: ");
	fprintf(fp, "%s", time);
	fprintf(fp, "\t%s\n", message);
	fprintf(fp, "____________________________________________\n");
	fclose(fp);						// Close the logging file.
	
}

void help(void)						// To print help to console 
{
	printf("\nLocal Logger\n");
	printf("Usage: log switch [message]\n");
	printf("switches:\n");
	printf("	init: will initialise the log file. The [message] field has\n");
	printf("	      to be the name of the logging file. _{present month} will\n");
	printf("		  be appended to the file name to keep track of months\n\n");
	printf("	-m  : will log your message to the log file. [message] has to be\n");
	printf("		  in single quotes only.\n\n");
	printf("	view: will show the present month's log\n\n");
	printf("Use log --help to print help\n\n");
	printf("Created by Vishwanath <vishwa.hyd@gmail.com>\n");
}

void view()						// This function will show the present month's log
{
	char *username;
	char abspath[MAXPATH];
		
	strcpy(abspath, "/home/");	// Extract information from .logfile about the logfile abs path
	username = getenv("USER");
	strcat(abspath, username);
	strcat(abspath, "/.logfile");
	
	FILE *info = fopen(abspath, "rb");
	char logpath[MAXPATH];
	
	fgets(logpath, MAXPATH, info);
	logpath[strlen(logpath) - 1] = '\0';
	puts(logpath);
	
	char command[MAXPATH + MAXLEN];		// The console command is $ cat filename | less
	strcpy(command, "cat ");
	strcat(command, logpath);
	strcat(command, " | less ");
	
	system(command);
}

int main(int argc, char **argv)
{
	if (argc <= 1)			// Return help instructions
	{
		printf("type log --help for usage\n");
		exit(1);
	}
	
	if (argc == 2)
	{
		if ( strcmp(argv[0], "sudo") == 0 )			// Ensure that the program is not executed with su previlages
		{
			printf("Don't use log with super user previlage\n");
			exit(1);
		}
		
		if (strcmp(argv[1], "--help") == 0)			// help command
		{
			help();
			exit(0);
		}
		
		if (strcmp(argv[1], "view") == 0)			// View the present month log
		{
			view();
			exit(0);
		}
		
		else										// Help instructions if garbage is typed!
		{
			printf("Type log --help for usage help\n");
			exit(1);
		}
		
		
	}
	
	if (argc == 3)
	{
		if ( strcmp(argv[0], "sudo") == 0 )			// Ensure that the program is not executed with su previlages
		{
			printf("Don't use log with super user previlage\n");
			exit(1);
		}
		
		if( strcmp(argv[1], "init") == 0)
		{
			log_init(argv[2]);
			exit(0);
		}
		
		if ( strcmp(argv[1], "-m") == 0)
		{
			writeLog(argv[2]);
			printf("Your message has been logged\n");
			exit(0);
		}
	}	
	else
	{
		printf("Message should be in single quotes. Use log --help\n");
		exit(1);
	}	
}
