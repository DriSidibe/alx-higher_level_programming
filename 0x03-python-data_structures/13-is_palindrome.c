#include <stdlib.h>
#include <math.h>
#include "lists.h"

/**
 * is_palindrome - verify if a singly list is palyndrome
 * @head: the list
 *
 * Return: 0 if is palyndrome
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0;
	listint_t *h = *head;
	int *list_int = NULL;

	if (*head == NULL)
		return (1);

	while (h != NULL)
	{
		len++;
		h = h->next;
	}

	h = *head;
	list_int = malloc(sizeof(int) * len);

	while (i != len)
	{
		list_int[i] = h->n;
		h = h->next;
		i++;
	}

	for (i = 0; i < round(len / 2); i++)
		if (list_int[i] != list_int[len - 1 - i])
			return (0);

	return (1);
}
