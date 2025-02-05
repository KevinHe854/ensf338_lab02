1. Mention at least two aspects that make interpolation search better than binary search.

        Interpolation search places the midpoint where the item is likely to occur, which can cut down the number of comparisons needed. Interpolation search can find the item faster than binary search as it already starts searching closer to where the item is.

2. Interpolation search assumes that data is uniformly distributed. What happens when this data follows a different distribution? Will the performance be affected?

        If the data is not unevenly distributed where there are varying gaps in between data items, interpolation search may take a while in searching in the areas where the gaps are larger. 

3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?

        Calculating pos in each iteration would be different so we can account for different gap sizes.

When comparing linear, binary and interpolation search:

4. When is linear search your only option for searching data as binary and interpolation search may fail?

        Linear search may be the only option when the array to search for isn't sorted.

5. In which case will linear search outperform both binary and interpolation search, and why?

        A case where linear search can outperform both binary and interpolation search is when the item to search for is at the start of the array. in this case, the complexity of a linear search is O(1), for binary and interpolation search is O(log2 (n)).

6. Is there a way to improve binary and interpolation search to solve this issue?

        We can probably add an additonal search that checks the "extremes" of the array (checking mid as well as low and high) whenever a subarray is searched.