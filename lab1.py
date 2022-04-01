import methods

text = """One, two, one, grt:   Mr. THREE. Four, five, six?     
Seven eight, nine ten M.B.!          """

k = 3 
n = 2

def main():
    sentences = methods.cutText(text)
    words = methods.cutSentences(sentences)
    nGrams = methods.grams(words, n, k)
    print(words)
    print(methods.meetWords(words))
    print(f"Median is {methods.averageLenght(words)[0]} \nThere are about {methods.averageLenght(words)[1]} words in one sentence")
    print(nGrams)

if __name__ == "__main__":
    main()