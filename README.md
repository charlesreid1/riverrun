# riverrun

Dense, incomprehensible Joycean tract that will keep the professors busy for centuries.

A [NaNoGenMo 2016](https://github.com/NaNoGenMo/2016) project.

**License:** Riverrun is released under an MIT License. 
It utilizes the [Olipy](https://github.com/leonardr/olipy/blob/master/COPYING) library, which is released under the GNU Public License v3.

## Turning Text into Data

**UlyssesTextToData.py**  - this script processes the Gutenberg Ulysses text 
and parses it into a data file that is readable by the Olipy library.

This process changes for some chapters, as (for example) Penelope (Ch. 18) 
consists of 5 extremely long run-on sentences, and must be split up in a different way.
Similarly, Aeolus (Ch. 7) must be parsed to separate newspaper headlines from the rest 
of the text.

This file defines a method for standard chapters, and a method for each chapter
that requires its own special treatment.

## Turning Data into a Novel

**QueneauNovel.py** - uses a queneau generator to create a new novel. 
Because the queneau generator uses the original novel as the corpus,
it works much better when generating a finished product smaller than
the original corpus.

**MarkovNovel.py** - uses a Markov generator to create a new novel.
This is much less sensible, has many more grammatical mistakes,
but generates much more interesting content.

## Turning a Novel into HTML

**MakeHTML.py** - a very, very simple script to dump out the contents
of a novel (in a Unicode text file) to an HTML file. This also correctly
handles Unicode symbols and translates them into the corresponding HTML codes.

