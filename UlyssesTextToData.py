import json
import re
import io 

chapter_names = ['telemachus',
        'nestor',
        'proteus',
        'calypso',
        'lotuseaters',
        'hades',
        'aeolus',
        'lestrygonians',
        'scyllacharybdis',
        'wanderingrocks',
        'sirens',
        'cyclops',
        'nausicaa',
        'oxenofthesun',
        'circe',
        'eumaeus',
        'ithaca',
        'penelope']


def std_chapter(n):
    if n>0 and n<19:
        txtfile = "txt/%02d%s.txt"%( n, chapter_names[n-1] )
        datfile = "data/%02d%s.dat"%( n, chapter_names[n-1] )

    # Load lines from file into list
    with io.open(txtfile,'r',encoding='utf-8') as f:
        oldparagraphs = f.readlines()

    paragraphs = []
    newline = ""
    for oldparagraph in oldparagraphs:
        if(oldparagraph <> "\n"): 
            # accumulate in newline variable
            newline = newline + re.sub("\n"," ",oldparagraph)
        else:
            # dump out newline variable and start it over again
            paragraphs.append(newline)
            newline = ""

    # Parse and output in json format 
    print("    Parsing for JSON...")
    with io.open(datfile,'w',encoding='utf-8') as o:
        paragraph_dictionaries = process_paragraphs(paragraphs,n)
    print("    Done parsing.")


    print("    Dumping to JSON...")
    with io.open(datfile,'w',encoding='utf-8') as o:

        for d in paragraph_dictionaries:

            # Dump dictionary to output file
            #json.dump(d, o, encoding='utf-8', ensure_ascii=False)
            result = json.dumps(d, encoding='utf-8')
            o.write(result.decode('utf-8'))
            o.write(u"\n")

    print("    Done dumping to JSON.")

    print("Done processing "+chapter_names[n-1])
    print("Input: "+txtfile)
    print("Output: "+datfile)
    print("\n")



def process_paragraphs(paragraphs, n):

    # One json object/"dictionary" per paragraph
    # {
    #    "parid" : <int>,
    #    "par" : "paragraph text goes here."
    # }

    paragraph_dictionaries = []

    if(n==17):
        # One json object/"dictionary" per paragraph
        for pp,paragraph in enumerate(paragraphs):
    
            # Turn the paragraph into a list of sentences
            sentences = paragraph.strip().split(". ")

            sentences = [s for s in sentences if len(s) > 1]

            if(len(sentences) > 0):

                # If the last character of the line is just a letter,
                # add a period at the end.
                for (i,s) in enumerate(sentences):
                    last_letter = s[len(s)-1]
                    if( last_letter.isalpha() ):
                        # Add the period back to the end
                        sentences[i] = sentences[i] + "."

                # Construct dictionary
                d = {}
                d['parid'] = pp
                d['par'] = sentences
                paragraph_dictionaries.append(d)
    
    if(n==18):
        # One json object/"dictionary" per paragraph
        for pp,paragraph in enumerate(paragraphs):
    
            # Turn the paragraph into a list of sentences
            fragments = paragraph.strip().split("I ")
            fragments = ["I "+j for j in fragments]
            
            # Construct dictionary
            d = {}
            d['parid'] = pp
            d['par'] = fragments
            paragraph_dictionaries.append(d)


    # All finished processing each paragraph... return text to put into JSON
    return paragraph_dictionaries




if __name__=="__main__":
    std_chapter(17)
    std_chapter(18)

