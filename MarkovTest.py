from olipy.markov import MarkovGenerator

if __name__ == '__main__':
    import sys
    with open('txt/01telemachus.txt','r') as f:
        generator = MarkovGenerator.loadlines(f, order=1, max=1000)
    for i in range(50):
        print " ".join(list(generator.assemble()))
