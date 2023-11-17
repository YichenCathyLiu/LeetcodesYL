class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.',"")
            return local+'@'+domain
        
        diary = []
        for i in emails:
            diary.append(parse(i))

        return len(set(diary))