#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: singly linked list to check
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	temp = list;

	if (!list)
		return (0);

	while (temp->next && temp)
	{
		if (temp->next == list)
			return (1);

		temp = temp->next;
	}

	return (0);
}
