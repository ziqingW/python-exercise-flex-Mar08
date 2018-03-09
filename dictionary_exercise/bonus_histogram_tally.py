def histogram_tally(word):
# make a function to return value from k,v pair 
    def takeValue(item):
        return item[1]
    
    result = {}
    for char in word:
        result[char] = word.count(char)
# make a list for k, v tuples
    itemList = [(k, v) for k, v in result.items()]
# sort the tuple list reversely by value only    
    itemList.sort(key = takeValue, reverse = True)
    for i in range(3):
        print("Top{} letter: {} -{} time(s).".format((i + 1), (itemList[i][0]), itemList[i][1]))

if __name__ == "__main__":
    histogram_tally(input("Give a word to start. ").lower())