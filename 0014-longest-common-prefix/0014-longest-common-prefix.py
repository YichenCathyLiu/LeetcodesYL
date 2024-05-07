class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # Check if the list of strings is empty
            return ""
                # Iterate through each string in the list

        prefix = strs[0]
        for string in strs:
            # Update the prefix while there is a mismatch or until the prefix is empty
            while not string.startswith(prefix):
                # Reduce the prefix by removing the last character
                prefix = prefix[:-1]
                if not prefix:  # If the prefix is empty, no common prefix exists
                    return ""
        
        # Return the final prefix after examining all strings
        return prefix