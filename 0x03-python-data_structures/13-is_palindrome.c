#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if listint_t list
 * @head: pointer to pointer of first node of list listint_t list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	unsigned int len = 1;
	listint_t *temp;

	if (head == NULL || *head == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (0);
}
