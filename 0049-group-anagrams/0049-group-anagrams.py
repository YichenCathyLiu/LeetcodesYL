class Solution:
    def groupAnagrams(self, strs):
        # 创建一个 defaultdict，默认值为一个空列表，用于存储字母异位词组
        anagram_map = defaultdict(list)
        
        # 遍历输入的字符串列表 strs
        for word in strs:
            # 对当前字符串 word 进行排序，并将排序后的字符列表组合成一个新的字符串 sorted_word
            sorted_word = ''.join(sorted(word))
            # 将原始字符串 word 添加到字典 anagram_map 中以 sorted_word 作为键的列表中
            anagram_map[sorted_word].append(word)

            # sorted_word就相当于成为了一个key，把所有的anagram都归类了
        
        # 将字典 anagram_map 中所有的值（即字母异位词组列表）转换为一个列表并返回
        return list(anagram_map.values())
