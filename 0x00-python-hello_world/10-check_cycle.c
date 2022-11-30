#include "lists.h"

/**
 * array_len - counts the length of a listint pointers array.
 * @arr: The array to count the length of.
 *
 * Return: The length of the array (success), -1 (error)
 */
ssize_t array_len(listint_t **arr)
{
	ssize_t len;

	if (arr == NULL)
		return (-1);
	for (len = 0; *arr != NULL; len++)
		arr++;
	return (len);
}

/**
 * array_malloc - allocats @size number of memory for listint_t pointers
 * and initializes their value to null and also adds 1 more for the
 * terminating NULL value of the array.
 * @size: The number  of memory to allocate
 *
 * Return: The address of the array (success), NULL (error)
 */
listint_t **array_malloc(size_t size)
{
	listint_t **memo = NULL;
	size_t i;

	if (size == 0)
		return (NULL);
	size = size + 1;
	memo = malloc(sizeof(listint_t *) * size);
	if (memo == NULL)
		return (NULL);
	for (i = 0; i < size; i++)
		memo[i] = NULL;
	return (memo);
}

/**
 * array_realloc - reallocats memory for a listint_t array by adding @size
 * size to the current value. and also it copies the old value to the newly
 * allocated place.
 * @arr_ptr: The address of the array.
 * @size: The size to add to the current size.
 *
 * Return: The address of the new array (success), NULL (error).
 */
listint_t **array_realloc(listint_t **arr_ptr, size_t size)
{
	listint_t **new = NULL;
	ssize_t tmp;

	if (arr_ptr == NULL || size == 0)
		return (arr_ptr);
	tmp = array_len(arr_ptr) + size; /* the size of the new memory */
	new = array_malloc(tmp);
	if (new == NULL)
		return (NULL);
	for (tmp = 0; arr_ptr[tmp] != NULL; tmp++)
		new[tmp] = arr_ptr[tmp];
	free(arr_ptr);
	return (new);
}

/**
 * check_cycle - checks if there is a cycle in a listint_t list.
 * @list: The head of the list to check cycle in.
 *
 * Return: 0 (no cycle or error), 1 (there is a cycle).
 */
int check_cycle(listint_t *list)
{
	listint_t **dump = NULL;
	ssize_t i, j;

	if (list == NULL || list->next == NULL)
		return (0);
	dump = array_malloc(50);
	if (dump == NULL)
		return (0);
	for (i = 0; list != NULL; list = list->next, i++)
	{
		for (j = 0; dump[j] != NULL; j++)
		{
			if (dump[j] == list)
			{
				free(dump);
				return (1);
			}
		}
		if (j == 50 * (i / 50) && i != 0)
			dump = array_realloc(dump, 50);
		dump[i] = list;
	}
	free(dump);
	return (0);
}
