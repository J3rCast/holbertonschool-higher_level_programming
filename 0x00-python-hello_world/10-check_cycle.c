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
	listint_t *temp, *tempNext;

	temp = list;
	tempNext = list;

	while (list && temp->next && tempNext->next->next)
	{
		if (temp->next == tempNext->next->next)
			return (1);

		temp = temp->next;
		tempNext = tempNext->next->next;
	}

	return (0);
}
