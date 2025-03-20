#include <stdio.h>
#include <stdlib.h>

int jide(int loop, int arr);
int main()
{
	int a, b;
	printf("Enter 2 numbers\nOne a loop and other no of arrays to create => ");
	scanf("%d %d", &a, &b);
	jide(a, b);
}
int jide(int loop, int arr)
{
	int **a;

	a = (int **) malloc(sizeof(int *) * arr);

	int i;
	int w = 0;
	for (; w < arr; w++)
	{
		printf("Enter the numbr of items to be added ");
		scanf("%d", &i);

		a[w] = (int *) malloc(sizeof(int) * i);

		int j;
		printf("Add the numbers with a space (e.g a b ...n)");
		for (j = 0; j < i; j++)
		{
			scanf("%d", &(a[w][j]));
		}
	}
	for (int s = 0; s < loop; s++)
	{
		int u,h;
		printf("Enter the array and particular position of an element in the array =>");
		scanf("%d %d", &u, &h);
		printf("The Element in the specified array = %d\n", a[u-1][h-1]);
	}

	free (a);
}
