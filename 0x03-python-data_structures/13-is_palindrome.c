#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - check whether a singly linked list is a palindrome
 *
 * @head: pointer to the head node
 *
 * Return: 1 if it's a palindrome, otherwise 0 (an empty list is considered
 * to be a palindrome)
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *new_head = NULL;
	listint_t *current = *head;
	listint_t *new_iterator;

	if (current == NULL)
		return (0);
	while (current)
	{
		add_nodeint(&new_head, current->n);
		current = current->next;
	}
	current = *head;
	new_iterator = new_head;
	while (current && new_iterator)
	{
		if (current->n != new_iterator->n)
			return (0);
		current = current->next;
		new_iterator = new_iterator->next;
	}

	free_listint(new_head);

	return (1);
}

/**
 * add_nodeint - add a new node to the beginning of a singly linked list
 *
 * @h: pointer to the head node
 * @n: integer element to assign to the new node
 *
 * Return: address of the new element, NULL if it fails
 */
listint_t *add_nodeint(listint_t **h, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (0);
	new_node->n = n;
	new_node->next = *h;
	*h = new_node;

	return (new_node);
}
