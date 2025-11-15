# What about implementhing this using "match" ?
#
# #include <iostream>
# using namespace std;
#
# int main()
# {
#   string textInput;
#
#   cout << "Enter a famous name+surname, ex. BarackObama: " << endl;
#   cin >> textInput;
#
#   if (textInput == "BarackObama")
#   { #     cout << "44th president of the United States" << endl; #   }
#   else if (textInput == "SandroPertini")
#   {
#     cout << "Former President of the Italian Republic" << endl;
#   }
#   else if (textInput == "NelsonMandela")
#   {
#     cout << "Former President of South Africa" << endl;
#   }
#   else if (textInput == "MahatmaGandhi")
#   {
#     cout << "Bapu" << endl;
#   }
#   else if (textInput == "DonaldKnuth")
#   {
#     cout << "Creator of LaTeX" << endl;
#   }
#   else if (textInput == "DennisRitchie")
#   {
#     cout << "Creator of C" << endl;
#   }
#   else
#   {
#     cout << "Invalid input! Please enter a good name!" << endl;
#   }
#
#   return 0;
# }
def print_output(text_input) -> None:
    match text_input:
        case "BarackObama":
            print("44th president of the United States")
        case "SandroPertini":
            print("Former President of the Italian Republic")
        case "NelsonMandela":
            print("Former President of South Africa")
        case "MahatmaGandhi":
            print("Bapu")
        case "DonaldKnuth":
            print("Creator of LaTeX")
        case "DennisRitchie":
            print("Creator of C")
        case _:
            print("Invalid input! Please enter a good name!")


def main():
    kb_input = str(input("Enter a famous name+surname, ex. BarackObama: "))
    print_output(kb_input)


if __name__ == "__main__":
    main()
