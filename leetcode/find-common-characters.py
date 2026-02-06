def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    count = {}
    for char in words[0]:
        count[char] = count.get(char, 0) + 1
        
        for word in words[1:]:
            temCount = {}
            for ch in word:
                temCount[ch] = temCount.get(ch, 0) + 1
            for ch in count:
                if ch in temCount:
                    min(count[ch],temCount[ch])
                else:
                    count[ch] = 0

    result = []
    for ch in count:
        result.extend([ch]*count[ch])
    return result
print(commonChars(["bella","label","roller"]))
print(commonChars(["cool","lock","cook"]))



