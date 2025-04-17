def students(first,last,id,english,math,history):
    """
    This function takes in lists of first names, last names, IDs, and grades in English, Math, and History.
    It returns a list of students with their average grade.
    """
    # Check if all lists are of the same length
    if not (len(first) == len(last) == len(id) == len(english) == len(math) == len(history)):
        raise ValueError("All input lists must have the same length.")

    # Create a list to store the final results
    finalList = []

    # Iterate through the lists and calculate the average for each student
    for i in range(len(first)):
        avg_grade = (english[i] + math[i] + history[i]) / 3
        finalList.append([first[i], last[i], id[i], avg_grade])
    for i in range(len(first)):
        finalList.append([first[i], last[i], id[i], (english[i] + math[i] + history[i]) / 3])

    return finalList
# Example usage
first = ['Tomer','Lia','Max','Noy']
last = ['Levi','Cohen','Sasson','Paz']
id = ['305674320','254667788','302123754','203818100']
english = [90, 88, 79, 99]
math = [100, 70, 85, 90]
history = [75, 96, 60, 98]
print(students(first, last, id, english, math, history))