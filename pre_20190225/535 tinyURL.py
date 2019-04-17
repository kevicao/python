# http://www.cnblogs.com/grandyang/p/6562209.html


#import pandas as pd
from random import randint

class tinyURL():

    def __init__(self, service, parent = None):
        
        self.cand = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.long_to_short = dict()
        self.short_to_long = dict()
        self.service = service
    
        print len(self.cand)
    
    def encoding(self, longURL):
        
        code = self.service
        for x in range(6):
            code += self.cand[randint(0, 62)]
            
        while code in self.short_to_long.keys():
            code = self.service
            for x in range(6):
                code += self.cand[randint(0, 62)] 
                
        self.short_to_long[code] = longURL
        
        print self.short_to_long
        
        self.decoding(code)
        
        return
        
    def decoding(self, shortURL):
        
        if shortURL in self.short_to_long.keys():
            print self.short_to_long[shortURL]
        else:
            print 'error'
        
        return
    
def main():
    
    service = 'http://tinyurl.com/'
    
    longURL = 'https://leetcode.com/problems/design-tinyurl'
    
    URL = tinyURL(service)
    URL.encoding(longURL)
    
    return

if __name__ == "__main__":
    main()


