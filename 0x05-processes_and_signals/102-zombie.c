#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - loop forever
 * Return: integer
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - function to create zombie processes
 * Return: integer
 */
int main(void)
{
	pid_t child_pid;
	int flag = 0;

	while (flag != 5)
	{
		child_pid = fork();
		if (child_pid > 0)
			printf("Zombie process created, PID: %d\n", child_pid);
		else if (child_pid == 0)
			exit(0);
		flag++;
	}
	infinite_while();
	return (0);
}
