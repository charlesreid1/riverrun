###########################################
# Riverrun: NaNoGenMo 2016 Novel
# Charles Reid 
# November 2016
#
# Chops up Ulysses to generate a new,
# dense, and incomprehensible tract.
###########################################

# Riverrun
import Constants as rr

# Olipy
from olipy.queneau import Assembler, CompositeAssembler, WordAssembler
from olipy.data import load_json

# Python stuff
import random

class Riverrun(object):
    """
    The Riverrun class generates the actual Riverrun novel.
    
    It does this in pieces: 
    * Create chapter
    * Create novel
    * Dump novel to text file
    * Dump novel to HTML file


    Algorithm:
    For each chapter:
        Generate chapter names
        Get file names
        Create generators
        For each paragraph:
            For each sentence:
                Generate new sentence
                Process all words to fix typos
                Add sentence to paragraph
            Add paragraph to chapter
        Add chapter to book
    """



    def make_chapter(self, chapter_number):
        """
        This method assembles the text of a single chapter,
        which lives within the object when the method is finished.
        """

        data_file = rr.data_files[chapter_number-1]
        text_file = rr.text_files[chapter_number-1]

        queneau_assembler = Assembler.loadlines(open(data_file), tokens_in='par')
        with io.open(text_file, 'r', encoding="utf-8") as f:
            markov_assembler = MarkovGenerator.loadlines(f, order=2, max=800)


        for i in range(Nparagraphs):





    def make_chapter_name(self):
        assembler = WordAssembler(load_json( rr.json_greek_names ))
        if( random.random() < 0.10 ):
            return assembler.assemble_word() + " and " + assembler.assemble_word()
        else:
            return assembler.assemble_word()




    def make_new_paragraph(assembler):
        pass






if __name__=="__main__":
    r = Riverrun()
    for i in range(50):
        print r.make_chapter_name()

