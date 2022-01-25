#include <stdio.h>

int main(void)
{
    int selection, period, total;
    int left_over_year, left_charge;
    int number_of_years_except_first;
    int yearly_costs;
    printf("Please select from the following menu: 1. Sofa, 2.Loveseat, 3. 4 Post Bed, 4. Dresser 5. Kitchen Table");

    printf("\nEnter furniture selection: ");
    scanf("%d", &selection);
    if (selection > 5 || selection < 1)
    {
        printf("\nInvalid input. The input should be in the range of 1 to 5");
        return 1;
    }

    printf("\nEnter months rented: ");
    scanf("%d", &period);

    if (period < 1)
    {
        printf("\nInvalid input. Enter a positive number for months rented");
        return 1;
    }

    if (selection == 1)
    {
        if (period <= 12)
        {
            total = 60 + (period - 1) * 45;
            if (total > 450)
            {
                total = 450;
            }
            else
            {
                total = total;
            }
        }
        else
        {
            total = 60 + 11 * 45;
            if (total > 450)
            {
                total = 450;
            }
            left_over_year = (period) % 12;
            left_charge = left_over_year * 45;
            if (left_charge > 450)
            {
                total += 450;
            }
            else
            {
                total += left_charge;
            }
            number_of_years_except_first = (period - 12) / 12;
            yearly_costs = 12 * 45;

            if (yearly_costs > 450)
            {
                total += 450 * number_of_years_except_first;
            }
            else
            {
                total += yearly_costs * number_of_years_except_first;
            }
        }
    }

    else if (selection == 2)
    {
        if (period <= 12)
        {
            total = 45 + (period - 1) * 30;
            if (total > 280)
            {
                total = 280;
            }
            else
            {
                total = total;
            }
        }
        else
        {
            total = 45 + 11 * 30;
            if (total > 280)
            {
                total = 280;
            }
            left_over_year = (period) % 12;
            left_charge = left_over_year * 30;
            if (left_charge > 280)
            {
                total += 280;
            }
            else
            {
                total += left_charge;
            }
            number_of_years_except_first = (period - 12) / 12;
            yearly_costs = 12 * 30;

            if (yearly_costs > 280)
            {
                total += 280 * number_of_years_except_first;
            }
            else
            {
                total += yearly_costs * number_of_years_except_first;
            }
        }
    }
    else if (selection == 3)
    {
        if (period <= 12)
        {
            total = 55 + (period - 1) * 38;
            if (total > 350)
            {
                total = 350;
            }
            else
            {
                total = total;
            }
        }
        else
        {
            total = 55 + 11 * 38;
            if (total > 350)
            {
                total = 350;
            }
            left_over_year = (period) % 12;
            left_charge = left_over_year * 38;
            if (left_charge > 350)
            {
                total += 350;
            }
            else
            {
                total += left_charge;
            }
            number_of_years_except_first = (period - 12) / 12;
            yearly_costs = 12 * 38;

            if (yearly_costs > 350)
            {
                total += 350 * number_of_years_except_first;
            }
            else
            {
                total += yearly_costs * number_of_years_except_first;
            }
        }
    }
    else if (selection == 4)
    {
        if (period <= 12)
        {
            total = 28 + (period - 1) * 25;
            if (total > 200)
            {
                total = 200;
            }
            else
            {
                total = total;
            }
        }
        else
        {
            total = 28 + 11 * 25;
            if (total > 200)
            {
                total = 200;
            }
            left_over_year = (period) % 12;
            left_charge = left_over_year * 25;
            if (left_charge > 200)
            {
                total += 200;
            }
            else
            {
                total += left_charge;
            }
            number_of_years_except_first = (period - 12) / 12;
            yearly_costs = 12 * 25;

            if (yearly_costs > 200)
            {
                total += 200 * number_of_years_except_first;
            }
            else
            {
                total += yearly_costs * number_of_years_except_first;
            }
        }
    }
    else if (selection == 5)
    {
        if (period <= 12)
        {
            total = 35 + (period - 1) * 20;
            if (total > 220)
            {
                total = 220;
            }
            else
            {
                total = total;
            }
        }
        else
        {
            total = 35 + 11 * 20;
            if (total > 220)
            {
                total = 220;
            }
            left_over_year = (period) % 12;
            left_charge = left_over_year * 20;
            if (left_charge > 220)
            {
                total += 220;
            }
            else
            {
                total += left_charge;
            }
            number_of_years_except_first = (period - 12) / 12;
            yearly_costs = 12 * 20;

            if (yearly_costs > 220)
            {
                total += 220 * number_of_years_except_first;
            }
            else
            {
                total += yearly_costs * number_of_years_except_first;
            }
        }
    }
    printf("Amount due ($): %d", total);
    return 0;
}
