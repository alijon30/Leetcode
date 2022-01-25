
#include <stdio.h>

int main(void)
{

    int given_year, years_passed, years_to_pass, next_appearance;
    printf("Enter year: ");
    scanf("%d", &given_year);

    if (given_year <= 1986)
    {
        printf("Input year must be greater than 1986");

        return 1;
    }

    years_passed = (given_year - 1986) % 76;
    years_to_pass = 76 - years_passed;
    next_appearance = years_to_pass + given_year;

    printf("Next apperance: %d", next_appearance);

    return 0;
}
