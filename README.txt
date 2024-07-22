1. first handle the sign of the number, storing whether it's negative and working with its absolute value.
2. convert the number to a string and sort its digits in ascending order.
3. find the first non-zero digit in the sorted list.
4. If the first digit is already non-zero, we can just join the sorted digits.
5. If there are leading zeros, we place the first non-zero digit at the beginning and arrange the rest of the digits (including zeros) after it.
Finally, we add back the negative sign if the original number was negative.