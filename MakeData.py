import json

files = ['01telemachus']

# Turn each chapter of Ulysses into a text file of dictionaries, with one dictionary per paragraph
for data_file in files:

    # Load lines from file into list
    with open('txt/'+data_file+'.txt','r') as f:
        paragraphs = f.readlines()
    
    # Parse and output in json format 
    with open('data/'+data_file+'.dat','w') as o:
    
        print("Processing "+data_file)

        # One json object/"dictionary" per paragraph
        for i,paragraph in enumerate(paragraphs):
    
            # Turn the paragraph into a list of sentences
            sentences = paragraph.strip().split(". ")
            ###sentences = paragraph.split(". ")
    
            # Only keep sentences longer than 1 character
            sentences = [s for s in sentences if len(s) > 1]

            # If the last character of the line is just a letter,
            # add a period at the end.
            for (i,s) in enumerate(sentences):
                last_letter = s[len(s)-1]
                if( last_letter.isalpha() ):
                    # Add the period back to the end
                    sentences[i] = sentences[i] + "."

            # Construct dictionary
            d = {}
            d['parid'] = i
            d['par'] = sentences
    
            # Dump dictionary to output file
            json.dump(d, o)
            o.write("\n")

print("All done!")
