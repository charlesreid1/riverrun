import json
import random
import re
import textwrap
import subprocess
import io


from olipy.queneau import Assembler, CompositeAssembler, WordAssembler

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



data_files = []
for i,e in enumerate(episode_names):
    data_files.append("data/%02d%s.dat"%(i+1,e.lower()))




money = []

for ii,data_file in enumerate(data_files):

    money.append("\n\n")
    money.append( " [ %02d %s ]"%(ii+1, episode_names[ii]) )
    money.append("\n\n")


    corpus = Assembler.loadlines(open(data_file))
    
    no_punctuation_at_end = re.compile("[a-zA-Z0-9]$")
    whitespace = re.compile("\s+")
    
    starts_with_letter = re.compile("^[a-zA-Z0-9].")

    contains_verse = re.compile("      ")

    how_many = int(round(random.random()*60))
    for i in range(how_many):
    
        sentences = []

        for line, source in corpus.assemble("m.l", min_length=12):

            if no_punctuation_at_end.search(line):
                if(data_file is '18penelope'):
                    line = line.strip() 
                else:
                    line = line.strip() + "."
    
            if contains_verse.search(line):
                verses = line.split("     ")
                verses = ["      "+v+"\n" for v in verses]
                for v in verses:
                    sentences.append(v)

            elif not starts_with_letter.search(line):
                sentences.append("\n")
                sentences.append(line)

            else:
                sentences.append(line)

                
    
        if(data_file is '18penelope'):
            par = "".join(sentences)
        else:
            par = " ".join(sentences)

        money.append(par)






money = [m.strip()+"\n" for m in money]
money = [m.encode('utf8') for m in money]

with open('my_novel.txt','w') as f:
    f.writelines(money)

