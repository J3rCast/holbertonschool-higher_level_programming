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

	temp = list->next;
	tempNext = list->next->next;

	if (!list || !list->next)
		return (0);

	while (temp && tempNext && tempNext->next)
	{
		if (temp == tempNext)
			return (1);

		temp = temp->next;
		tempNext = tempNext->next->next;
	}

	return (0);
}
