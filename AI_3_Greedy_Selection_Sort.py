
#################################################################################################

# Problem Statement:

''' Implement Greedy Search Algorithm for Selection Sort. '''

#################################################################################################

# Function to perform the Selection Sort based on user choice (Ascending / Descending)

def selection_sort(lst, order="asc"):
    n = len(lst)
    for i in range(0,n-1,1):
        for j in range(i+1,n,1):
            if (
                (order == "asc" and lst[i] > lst[j]) or
                (order == "desc" and lst[i] < lst[j])
            ):
                lst[i], lst[j] = lst[j], lst[i]
        # Print current state after each pass
        print(f"\n After Pass {i + 1} : {lst}\n")
    return lst

#<------------------------------------------------------------------------------

# Driver Code
def driver():

    n = int(input("\n Enter the number of elements in List : "))

    if(n>0):
        input_list = []
        for i in range(n):
            element = int(input(f"\n Enter element {i+1} : "))
            input_list.append(element)

        order = input("\n In which order you want to sort the list? (asc/desc) : ").lower()

        while (order not in ["asc", "desc"]):
            order = input("\n Invalid input! Please enter 'asc' or 'desc' : ").lower()

        print("\n Original List : ")
        print("\n ",input_list)

        print(f"\n Sorting list in the {'Ascending' if order == 'asc' else 'Descending'} Order using Selection Sort :")
        sorted_list = selection_sort(input_list, order)

        print("\n Final Sorted List : ")
        print("\n ",sorted_list)
        print("\n Thank You! (-_-)\n")
    else:
        print("\n Oops! Please Try Again! \n")
#<------------------------------------------------------------------------------

# Run the program
if __name__ == "__main__":
    driver()

#################################################################################################