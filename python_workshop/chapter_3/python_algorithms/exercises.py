#Exercise 39 – finding the maximum number
numbers=[4,2,7,3]
def maximum(numbers):
    maximum=0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
print(maximum(numbers))
#Exercise 40 – using bubble sort in Python Time_Complexity=O(n^2)
def bubble_sort(numbers):
    swapping_status=True
    while swapping_status:
        swapping_status=False
        for index in range(len(numbers)-1):
            if numbers[index]>numbers[index+1]:
                numbers[index],numbers[index+1]=numbers[index+1], numbers[index]
                swapping_status=True
    return numbers
print(bubble_sort(numbers))
#Exercise 41 – linear search in Python => O(n)
def linear_search(items,search_for):
    for item in items:
        if item == search_for:
            return items.index(item)
        else:
            return "item not found"
print(linear_search(numbers,2))
#Exercise 42 – binary search in Python
sorted_list = [2, 3, 5, 8, 11, 12, 18]
def binary_search(sorted_list,search_for):
    slice_start=0
    slice_end=len(sorted_list)-1
    found = False
    
    while slice_start<=slice_end and not found:
        location=(slice_start+slice_end)//2
        if sorted_list[location]== search_for:
            found=True
            return location
        else:
            if search_for < sorted_list[location]:
                slice_end=location-1
            else:
                slice_start=location+1
    
print(binary_search(sorted_list,5))