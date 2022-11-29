#include "lists.h"

/**
 * check_cycle - checks whether singly linked list has a loop
 * @list : points to head node
 * Return: 1 if linked list has a loop, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;

	if (!list)
		return (0);
	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
