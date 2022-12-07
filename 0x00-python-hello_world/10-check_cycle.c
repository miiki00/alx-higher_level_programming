#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a listint_t list.
 * @list: The head of the list to check cycle in.
 *
 * Return: 0 (no cycle or error), 1 (there is a cycle).
 */
int check_cycle(listint_t *list)
{
	listint_t *dump = NULL, *copy = NULL;
	ssize_t i, j;

	if (list == NULL || list->next == NULL)
		return (0);
	for (i = 0, copy = list; copy != NULL; copy = copy->next, i++)
	{
		for (dump = list, j = 0; j != i; dump = dump->next, j++)
		{
			if (dump == copy)
				return (1);
		}
	}
	return (0);
}
