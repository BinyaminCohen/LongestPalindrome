from collections import Counter


def longestPalindrome(s):
    try:
        if not isinstance(s, str):
            raise ValueError("Input must be an string!")
        else:
            char_count = Counter(s)
            palindrome_length = 0
            odd_center_used = False        # To track if we've used an odd character in the center

            for count in char_count.values():
                if count % 2 == 0:
                    palindrome_length += count  # Add even counts fully
                else:
                    palindrome_length += count - 1  # Add the largest even number less than the odd count
                    odd_center_used = True  # Mark that we have at least one odd count

            if odd_center_used:
                palindrome_length += 1

            return palindrome_length

    except(ValueError, TypeError) as e:
        # Handle the error by printing an error message
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    print(longestPalindrome("abccccdd"))  # Output: 7 (dccaccd)
    print(longestPalindrome("AaBb"))  # Output: 1 (no palindromes longer than 1 character)
    print(longestPalindrome("a"))  # Output: 1 (a)
    print(longestPalindrome("AaBbCc"))  # Output: 1 (any single character)
    print(longestPalindrome("Nitin"))  # Output: 5 (either Nitin or nitin or some case variation)
    print(longestPalindrome("aA"))  # Should return 1 (case sensitive)
    print(longestPalindrome("aaAA"))  # Should return 4 (all characters can be used)
    print(longestPalindrome("abcABC"))  # Should return 1 (only one character can be in the center)
    print(longestPalindrome(23))  # Output: 5 (either Nitin or nitin or some case variation)
