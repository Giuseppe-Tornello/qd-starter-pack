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
month_day = int(input("Enter month number(1-12): "))

months_31 = [1,3,5,7,8,10,12]
months_30 = [11,4,6,9]
months_28 = 2

if month_day in months_31:
    print("31 days")
elif month_day in months_30:
    print("30 days")
elif month_day == months_28:
    print("28 days")
else:
    print("Invalid input! Please enter month number between 1-12")
