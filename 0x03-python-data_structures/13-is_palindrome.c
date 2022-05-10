#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * reverse - reverse a linked list
 *
 * @head: header of the lintked list
 * @listSize: Size of the linked list
 *
 * Return: an array of ints reversed
 */
int *reverse(listint_t **head, int listSize)
{
	int *dataReversed = 0;

	listint_t *temp;

	temp = *head;

	dataReversed = malloc(sizeof(int) * listSize + 1);
	if (!dataReversed)
		return (NULL);

	while (temp != NULL)
	{
		dataReversed[listSize] = temp->n;
		temp = temp->next;
		listSize--;
	}
	return (dataReversed);
}
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
		return (1);
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
	listSize--;
	temp = *head;
	while (temp != NULL)
	{
		data[i] = temp->n;
		temp = temp->next;
		i++;
	}
	dataReversed = reverse(head, listSize);
	data[i] = '\0', dataReversed[i] = '\0', i = 0;
	while (data[i] == dataReversed[i])
	{
		if (!data[i] || !dataReversed[i])
		{
			free(data);
			free(dataReversed);
			return (1);
		}
		i++;
	}
	free(data);
	free(dataReversed);
	return (0);
}
