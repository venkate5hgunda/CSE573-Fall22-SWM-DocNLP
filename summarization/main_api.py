# import requests

# API_TOKEN = "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"
# API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
	
# output = query({
# 	"inputs": """ From: admiral@jhunix.hcf.jhu.edu (Steve C Liu)
# Subject: Baseball Stats

# 	Hello, my friends and I are running the Homewood Fantasy Baseball
# League (pure fantasy baseball teams). Unfortunely, we are running the league
# using Earl Weaver Baseball II with the Comm. Disk II and we need the stats
# for the 1992 season. (Preferably the 1992 Major League Stat Disk) We have
# the '92 total stats but EWB2 needs the split stats otherwise we have 200
# inning games because the Comm. Disk turns total stats into vs. L's stats
# unless you know both right and left -handed stats.

# 	So, if anyone has the EWB2 '92 Stat Disk please e-mail me!
# __________________________________________________________________________
# |Admiral Steve C. Liu        Internet Address: admiral@jhunix.hcf.jhu.edu|
# |"Committee for the Liberation and Intergration of Terrifying Organisms  |
# |and their Rehabilitation Into Society" from Red Dwarf - "Polymorph"     |
# |****The Bangles are the greatest female rock band that ever existed!****|
# |   This sig has been brought to you by... Frungy! The Sport of Kings!   |
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  """,
#     "parameters": {"min_length":30, "max_length":130}
# })

# print(output[0]['summary_text'])

# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ARTICLE = """Archive-name: atheism/resources Alt-atheism-archive-name: resources Last-modified: 11 December 1992 Version: 1.0  Atheist Resources  Addresses of Atheist Organizations  USA  FREEDOM FROM RELIGION FOUNDATION  Darwin fish bumper stickers and assorted other atheist paraphernalia are available from the Freedom From Religion Foundation in the US.  Write to:  FFRF, P.O. Box 750, Madison, WI 53701. Telephone: (608) 256-8900  EVOLUTION DESIGNS  Evolution Designs sell the "Darwin fish".  It's a fish symbol, like the ones Christians stick on their cars, but with feet and the word "Darwin" written inside.  The deluxe moulded 3D plastic fish is $4.95 postpaid in the US.  Write to:  Evolution Designs, 7119 Laurel Canyon #4, North Hollywood, CA 91605.  People in the San Francisco Bay area can get Darwin Fish from Lynn Gold -- try mailing <figmo@netcom.com>.  For net people who go to Lynn directly, the price is $4.95 per fish.  AMERICAN ATHEIST PRESS  AAP publish various atheist books -- critiques of the Bible, lists of Biblical contradictions, and so on.  One such book is:  "The Bible Handbook" by W.P. Ball and G.W. Foote.  American Atheist Press. 372 pp.  ISBN 0-910309-26-4, 2nd edition, 1986.  Bible contradictions, absurdities, atrocities, immoralities... contains Ball, Foote: "The Bible Contradicts Itself", AAP.  Based on the King James version of the Bible.  Write to:  American Atheist Press, P.O. Box 140195, Austin, TX 78714-0195. or:  7215 Cameron Road, Austin, TX 78752-2973. Telephone: (512) 458-1244 Fax:       (512) 467-9525  PROMETHEUS BOOKS  Sell books including Haught's "Holy Horrors" (see below).  Write to:  700 East Amherst Street, Buffalo, New York 14215. Telephone: (716) 837-2475.  An alternate address (which may be newer or older) is: Prometheus Books, 59 Glenn Drive, Buffalo, NY 14228-2197.  AFRICAN-AMERICANS FOR HUMANISM  An organization promoting black secular humanism and uncovering the history of black freethought.  They publish a quarterly newsletter, AAH EXAMINER.  Write to:  Norm R. Allen, Jr., African Americans for Humanism, P.O. Box 664, Buffalo, NY 14226.  United Kingdom  Rationalist Press Association          National Secular Society 88 Islington High Street               702 Holloway Road London N1 8EW                          London N19 3NL 071 226 7251                           071 272 1266  British Humanist Association           South Place Ethical Society 14 Lamb's Conduit Passage              Conway Hall London WC1R 4RH                        Red Lion Square 071 430 0908                           London WC1R 4RL fax 071 430 1271                       071 831 7723  The National Secular Society publish "The Freethinker", a monthly magazine founded in 1881.  Germany  IBKA e.V. Internationaler Bund der Konfessionslosen und Atheisten Postfach 880, D-1000 Berlin 41. Germany.  IBKA publish a journal: MIZ. (Materialien und Informationen zur Zeit. Politisches Journal der Konfessionslosesn und Atheisten. Hrsg. IBKA e.V.) MIZ-Vertrieb, Postfach 880, D-1000 Berlin 41. Germany.Politisches Journal der Konfessionslosesn und Atheisten. Hrsg. IBKA e.V.) MIZ-Vertrieb.
# """
# print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
# # [{'summary_text': 'Liana Barrientos, 39, is charged with two counts of "offering a false instrument for filing in the first degree" In total, she has been married 10 times, with nine of her marriages occurring between 1999 and 2002. She is believed to still be married to four men.'}]

import numpy as np
import time
import os
from numpy import save
from numpy import load

# fName = "C://Users//kuppala2//Desktop//SWM//cluster_folder"
# epoch_time = str(int(time.time()))

# listOut = list()

# for path in os.listdir(fName):
# 	if os.path.isfile(os.path.join(fName, path)):
# 		text_file = open(os.path.join(fName, path), "r")
# 		data = text_file.read()
# 		text_file.close()
# 		listOut.append([path, data])

# save('clusterData.npy', listOut)
# print(listOut)


data = load('clusterData.npy')
print(data)
