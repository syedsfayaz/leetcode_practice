
x = "babad"


def longestPalindrome(s) -> str:
    string_len = len(s)
    if string_len == 0:
        return ""
    if string_len == 1:
        return s
    if s == s[::-1]:
        return s
    i = 0
    stored_dict = {}
    while i < (string_len):
        for j in range(i, string_len+1):
            temp_val = s[i:j]
            tem_cnt = len(s[i:j])
            if s[i:j] == s[i:j][::-1] and len(s[i:j]) not in stored_dict:
                stored_dict[len(s[i:j])] = s[i:j][::-1]
        i += 1
    #max_val = max(stored_dict)
    #print(stored_dict)
    return(stored_dict[max(stored_dict)])

print(longestPalindrome("babababx"))

# def longestPalindrome(s) -> str:
#     ## babad
#      for i in len(s):
#          if i
