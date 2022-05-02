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

	while (temp->next != NULL && temp->next != list)
		temp = temp->next;
	if (temp->next == list)
		return (1);
	return (0);
}
