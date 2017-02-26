###########################################
# Riverrun: Constants
# Charles Reid 
# November 2016
# 
# Defines quantities useful to Riverrun
# (chapter names, file locations, etc.)
#
###########################################

### Chapters ###
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

### File paths ###
full_path = "/Volumes/noospace/Users/charles/codes/riverrun/"

json_greek_names = "%s/data/greeknames.json"%(full_path)

text_files = []
data_files = []
for i,e in enumerate(episode_names):
    text_files.append("%s/txt/%02d%s.txt"%( full_path, i+1, e.lower()))
    data_files.append("%s/data/%02d%s.dat"%(full_path, i+1, e.lower()))

