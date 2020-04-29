#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *head;

if (list == NULL)
return (0);
head = list;
while (head->next && list)
{
head = head->next;
}
if (head == NULL)
return (1);

return (0);
}
