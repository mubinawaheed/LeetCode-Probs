def countNodes(self):
    def Count(root, count):

        if(root is None):
            return 0
        count+=1
        if(root.lc is not None):
            
            count=Count(root.lc, count)
        
        if(root.rc is not None):
            count=Count(root.rc, count)
        return count

    c=Count(self, 0)
    return c
