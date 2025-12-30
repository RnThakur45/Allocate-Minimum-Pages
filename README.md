# Allocate-Minimum-Pages
https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

📝 Problem Statement

Given an array arr[] where each element represents the number of pages in a book, and an integer k representing the number of students, allocate books such that:

    Each student gets at least one book

    Books assigned to a student are contiguous

    No book is shared between students

    The maximum pages assigned to any student is minimized

If allocation is not possible, return -1.

💡 Approach: Binary Search on Answer

This problem is solved efficiently using Binary Search because:

    The minimum pages a student can get is max(arr)

    The maximum pages a student can get is sum(arr)

We search within this range to find the smallest possible maximum pages that can be allocated.

🔍 Feasibility Check

For a given maximum page limit:

    Allocate books sequentially

    Start a new student when the current sum exceeds the limit

    If more than k students are required, allocation is invalid

⚙️ Algorithm Steps

If k > number of books, return -1

Set:

    low = max(arr)

    high = sum(arr)

    Perform binary search:

    If allocation is possible, try a smaller maximum

    Otherwise, increase the limit

    Return the minimum valid maximum pages