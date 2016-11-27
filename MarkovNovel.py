import json
import random
import re
import textwrap
import subprocess
import io

from olipy.markov import MarkovGenerator

episode_names = [ "Telemachus",
        "Nestor",
        "Proteus",
        "Calypso",
        "LotusEaters",
        "Hades",
        "Aeolus",
        "Lestrygonians",
        "ScyllaCharybdis",
        "WanderingRocks",
        "Sirens",
        "Cyclops",
        "Nausicaa",
        "OxenOfTheSun",
        "Circe",
        "Eumaeus",
        "Ithaca",
        "Penelope"]


text_files = []
for i,e in enumerate(episode_names):
    text_files.append("txt/%02d%s.txt"%(i+1,e.lower()))


money = []

for ii,text_file in enumerate(text_files):

    money.append("\n\n")
    money.append( " [ %02d %s ]"%(ii+1, episode_names[ii]) )
    money.append("\n\n")

    with open(text_file,'r') as f:
        generator = MarkovGenerator.loadlines(f, order=1, max=200)

    how_many_paragraphs = int(round(random.random()*80))
    how_many_sentences = int(round(random.random()*30))

    for iip in range(how_many_paragraphs):

        sentences = []

        for iis in range(how_many_sentences):

            sentence = list(generator.assemble())
            sent = " ".join(sentence)

            sentences.append(sent)

        money.append(" ".join(sentences))
        
        money.append("\n")




    ### ###########################
    ### # start over.

    ### z = list(generator.assemble())

    ### # Use this search,
    ### # but if it's found,
    ### # insert a new line.
    ### print [re.sub("\xe2\x80\x94","-",zz) for zz in z]

    ### ###no_punctuation_at_end = re.compile("[a-zA-Z0-9]$")




    ###no_punctuation_at_end = re.compile("[a-zA-Z0-9]$")
    ###whitespace = re.compile("\s+")
    ###
    ###starts_with_letter = re.compile("^[a-zA-Z0-9].")

    ###contains_verse = re.compile("      ")

    ###how_many_paragraphs = int(round(random.random()*80))

    ###how_many_sentences = int(round(random.random()*30))

    ###for i in range(how_many_paragraphs):
    ###
    ###    sentences = []

    ###    for sentence in range(how_many_sentences):
    ###        
    ###        for word in list(generator.assemble()):

    ###            if no_punctuation_at_end.search(word):
    ###                word = word.strip()

    ###                sentences.append(word)


    ###    par = " ".join(sentences)

    ###    if not starts_with_letter.search(par): 
    ###        money.append("\n")
    ###    
    ###    money.append(par)


money = [m.strip()+"\n" for m in money]
#money = [m.encode('utf8') for m in money]

with open('markov_novel.txt','w') as f:
    f.writelines(money)


