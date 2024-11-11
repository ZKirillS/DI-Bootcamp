# Daily Challenge : Pagination

class Pagination:
    def __init__(self,items=None,pageSize=10):
        if items is None:
            items=[]
        self.items = items
        self.pageSize = int(pageSize)
        self.totalItems = len(items)
        self.totalPages = (self.totalItems+self.pageSize-1)//self.pageSize
        self.currentPage=1

    def getVisibleItems(self):
        start=(self.currentPage-1)*self.pageSize
        end = start+self.pageSize
        return self.items[start:end]
    
    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self
    
    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self
    
    def firstPage(self):
        self.currentPage=1
        return self
    
    def lastPage(self):
        self.currentPage=self.totalPages
        return self
    
    def goToPage(self,pageNum):
        pageNum = int(pageNum)
        if pageNum <1:
            self.currentPage = 1
        elif pageNum>self.totalPages:
            self.currentPage=self.totalPages
        else:
            self.currentPage = pageNum
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p=Pagination(alphabetList,4)
print(p.getVisibleItems())
p.nextPage
print(p.getVisibleItems())
p.lastPage
print(p.getVisibleItems())
p.firstPage
print(p.getVisibleItems())
p.goToPage(3)
print(p.getVisibleItems())
p.goToPage(10)
print(p.getVisibleItems())
p.goToPage(-5)
print(p.getVisibleItems())