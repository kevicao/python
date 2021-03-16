#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import defaultdict

def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """

    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0

    # Since all words are of same length.
    L = len(beginWord)

    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word.
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

    print(all_combo_dict)
    # Queue for BFS
    queue = [(beginWord, 1)]
    # Visited to make sure we don't repeat processing same word.
    visited = {beginWord: True}
    while queue:
        print(queue)
        current_word, level = queue.pop(0)  #pop the first element, but insert at the end later
        print(queue, current_word)
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            print(intermediate_word)

            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[intermediate_word] = []
    return 0

ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"])


# In[6]:


#find all shortest path
# https://www.cnblogs.com/grandyang/p/4548184.html
#https://fizzbuzzed.com/top-interview-questions-4/

findLadders(beginWord, endWord, wordList):
    res = []
    unordered_set<string> dict(wordList.begin(), wordList.end());
    vector<string> p{beginWord};
    queue<vector<string>> paths;
    paths.push(p)
    
    int level = 1, minLevel = INT_MAX;
    unordered_set = set(words)
    while !paths.empty():
        t = paths.pop(0);
        if (t.size() > level) {
            for (string w : words) dict.erase(w);
            words.clear();
            level = t.size();
            if (level > minLevel) break;
        }
        string last = t.back();
        for (int i = 0; i < last.size(); ++i) {
            string newLast = last;
            for (char ch = 'a'; ch <= 'z'; ++ch) {
                newLast[i] = ch;
                if (!dict.count(newLast)) continue;
                words.insert(newLast);
                vector<string> nextPath = t;
                nextPath.push_back(newLast);
                if (newLast == endWord) {
                    res.push_back(nextPath);
                    minLevel = level;
                } else paths.push(nextPath);
            }
        }
    }
    return res;
}
}


# In[ ]:




