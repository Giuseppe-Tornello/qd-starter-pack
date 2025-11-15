# Surprise me.
#
# #include <stdio.h>
#
# int main()
# {
#   int month;
#
#   /* Input month number from user */
#   printf("Enter month number(1-12): ");
#   scanf("%d", &month);
#
#   switch (month)
#   {
#   case 1:
#     printf("31 days");
#     break;
#   case 2:
#     printf("28/29 days");
#     break;
#   case 3:
#     printf("31 days");
#     break;
#   case 4:
#     printf("30 days");
#     break;
#   case 5:
#     printf("31 days");
#     break;
#   case 6:
#     printf("30 days");
#     break;
#   case 7:
#     printf("31 days");
#     break;
#   case 8:
#     printf("31 days");
#     break;
#   case 9:
#     printf("30 days");
#     break;
#   case 10:
#     printf("31 days");
#     break;
#   case 11:
#     printf("30 days");
#     break;
#   case 12:
#     printf("31 days");
#     break;
#   default:
#     printf("Invalid input! Please enter month number between 1-12");
#   }
#
#   return 0;
# }
def print_month_days(month_number: int) -> None:
    """Given a month (int 1-12) this function prints the number of days"""
    months_31_list = [1,3,5,7,8,10,12]
    months_30_list = [11,4,6,9]
    months_28 = 2

    if month_number in months_31_list:
        print("31 days")
    elif month_number in months_30_list:
        print("30 days")
    elif month_number == months_28:
        print("28/29 days")
    else:
        print("Invalid input! Please enter month number between 1-12")


def main():
    month = int(input("Enter month number(1-12): "))
    print_month_days(month)


if __name__ == "__main__":
    main()
