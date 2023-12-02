#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);

	listint_t *end = *head;

	return (aux_palindrome(head, end));
}

/**
 * aux_palindrome - recursive function to check if linked list is a palindrome
 * @head: head of the linked list
 * @end: end of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int aux_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);

	if (aux_palindrome(head, end->next) && (*head)->data == end->data)
	{
		*head = (*head)->next;
		return (1);
	}

	return (0);
}
