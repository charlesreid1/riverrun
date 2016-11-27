import json
from olipy.queneau import WordAssembler
from olipy.data import load_json
import textwrap

my_json_file = "/Volumes/noospace/Users/charles/codes/riverrun/data/greeknames.json"

assembler = WordAssembler(load_json( my_json_file ))

for i in range(18):

    greek = assembler.assemble_word()
    
    print("Chapter %d: %s"%(i+1,greek)) 

