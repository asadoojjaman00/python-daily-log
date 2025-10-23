# Problem: Longest Substring Without Repeating Characters ✅

def longest_unique_substring(s):
    # 1️⃣ Initialize variables
    char_set = set()   # এই set এ আমরা current substring এর characters রাখব
    left = 0           # substring start pointer
    max_length = 0     # longest substring length track করার জন্য

    # 2️⃣ Loop through string using 'right' pointer
    for right in range(len(s)):
        # যদি current character set এ থাকে, left pointer বাড়াও যতক্ষণ duplicate remove না হয়
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # current character add করো set এ
        char_set.add(s[right])

        # update max_length
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
string_input = "abcabcbb"
print(f"Longest unique substring length: {longest_unique_substring(string_input)}")
