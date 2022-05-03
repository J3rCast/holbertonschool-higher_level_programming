#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the linked list
 * @number: number value of the new node
 *
 * Return: new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *next, *new;

	if (head == NULL || *head == NULL)
		return (NULL);

	current = *head;
	next = current->next;

	while (number > next->n)
	{
		current = current->next;
		next = next->next;
	}
	new = malloc(sizeof(*head));
	if (new == NULL)
		return (NULL);
	new->next = next;
	current->next = new;
	new->n = number;

	return (new);
}
