class Solution:

    def sortColors(self, nums: list[int]) -> None:

        """
        Do not return anything.
        Modify nums in-place.
        """

        # low  -> position where the next 0 should be placed
        # mid  -> current element we are checking
        # high -> position where the next 2 should be placed

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            # ------------------------------------------------
            # CASE 1: Current element is 0
            # ------------------------------------------------
            if nums[mid] == 0:

                # Put 0 at the 'low' position
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp

                # We have successfully placed a 0
                low += 1

                # Current element is also processed
                mid += 1


            # ------------------------------------------------
            # CASE 2: Current element is 1
            # ------------------------------------------------
            elif nums[mid] == 1:

                # 1 belongs in the middle.
                # Nothing needs to be swapped.
                mid += 1


            # ------------------------------------------------
            # CASE 3: Current element is 2
            # ------------------------------------------------
            else:

                # Put 2 at the 'high' position
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp

                # 2 has been placed at the correct end
                high -= 1

                # IMPORTANT:
                # Do NOT do mid += 1 here.
                #
                # Why?
                # The element that came from nums[high]
                # is now at nums[mid].
                # We haven't checked that element yet.