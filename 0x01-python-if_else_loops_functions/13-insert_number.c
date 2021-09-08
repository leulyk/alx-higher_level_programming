#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert a node into a sorted singly linked list
 *
 * @head: pointer to the head node
 * @number: the new node's integer data
 *
 * Return: address of the new node, NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	current = *head;
	if (*head == NULL || number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->next == NULL)
		{
			current->next = new;
			new->next = NULL;
			return (new);
		}
		else if (number >= current->n && number <= current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}

	return (NULL);
}
