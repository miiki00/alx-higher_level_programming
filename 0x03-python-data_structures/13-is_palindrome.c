#include "lists.h"

/**
 * listLength - measres the length of a list
 * @head: the head of the list.
 *
 * Return: The length of the list.
 */
ssize_t listLength(listint_t *head)
{
	ssize_t length;

	if (head == NULL)
		return (0);
	length = 0;
	while (head != NULL)
	{
		head = head->next;
		length++;
	}
	return (length);
}

/**
 * is_palindrome - checks if a list is palidrome or not.
 * @head: The head of the list.
 *
 * Return: 0 if not palindrom, 1 if palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *top = NULL, *bottom = NULL;
	ssize_t up, length, i, j;

	if (head == NULL || *head == NULL)
		return (1);
	length = listLength(*head);
	top = *head;
	for (i = 0, up = length - 1; i < length / 2; i++, top = top->next, up--)
	{
		for (j = 0, bottom = *head; j < up; j++)
			bottom = bottom->next;
		if (top->n != bottom->n)
			return (0);
	}
	return (1);

}
