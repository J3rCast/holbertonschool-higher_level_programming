#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 *
 * Return: 0 if is not, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int listSize = 0, i = 0;
	int *dataReversed = 0, *data = 0;

	if (head == NULL)
		return (0);
	listint_t *temp;

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		listSize++;
	}
	data = malloc(sizeof(int) * listSize + 1);
	if (!data)
		return (1);
	dataReversed = malloc(sizeof(int) * listSize + 1);
	if (!dataReversed)
	return (1);
	listSize--;
	temp = *head;
	while (temp != NULL)
	{
		data[i] = temp->n;
		dataReversed[listSize] = temp->n;
		temp = temp->next;
		i++;
		listSize--;
	}
	data[i] = '\0';
	dataReversed[i] = '\0';
	i = 0;
	while (data[i] == dataReversed[i])
	{
		if (!data[i] || !dataReversed[i])
			return (1);
		i++;
	}
	return (0);
}
