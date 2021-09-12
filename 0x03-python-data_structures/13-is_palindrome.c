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
	listint_t *current = *head;
	int i = 0, length = 0, *list;

	if (current == NULL)
		return (1);
	while (current)
	{
		current = current->next;
		length++;
	}
	list = malloc(sizeof(int) * length);
	if (list == NULL)
		return (0);
	current = *head;
	i = 0;
	while (current)
	{
		list[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0; i <= (length - 1) / 2; ++i)
	{
		if (list[i] != list[length - 1 - i])
		{
			free(list);
			return (0);
		}
	}
	free(list);

	return (1);
}
