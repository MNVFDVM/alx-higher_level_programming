#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *p = NULL;
	listint_t *c = *head;
	listint_t *next = NULL;

	while (c)
	{
		next = c->next;
		c->next = p;
		p = c;
		c = next;
	}

	*head = p;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *f = *head, *t = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		f = f->next->next;
		if (!f)
		{
			dup = s->next;
			break;
		}
		if (!f->next)
		{
			dup = s->next->next;
			break;
		}
		s = s->next;
	}

	reverse_listint(&dup);

	while (dup && t)
	{
		if (t->n == dup->n)
		{
			dup = dup->next;
			t = t->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
