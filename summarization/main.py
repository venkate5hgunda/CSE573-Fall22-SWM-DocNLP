from transformers import pipeline
import re
import os
import random
import time    

class Summary:
    def __init__(self, folderNameInput, fileNameOutput):
        self.summaryOutput = None
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.folderNameInput = folderNameInput
        self.fileNameOutput = fileNameOutput
        self.fstr = ""
        self.counter = 1

    def removeLines(self, fileName):
        # self.fstr = ""
        self.counter += 1
        print(fileName, self.counter)
        ffile = open(fileName, 'r')
        for line in ffile.readlines():
            xfrom = re.findall("^From", line)
            ysubject = re.findall("^Subject", line)

            if not xfrom and not ysubject:
                self.fstr += line.strip() + " "
    
    def iterateFolder(self):
        ffile1 = open(self.fileNameOutput, 'w')
        # for path in os.listdir(self.folderNameInput):
        #     if os.path.isfile(os.path.join(self.folderNameInput, path)):
        #         self.removeLines(os.path.join(self.folderNameInput,path))
        for i in range(20):
            randFile = random.choice(os.listdir(self.folderNameInput))
            self.removeLines(os.path.join(self.folderNameInput,randFile))
        i = 0
        ln = len(self.fstr)
        while((i+3000)<len(self.fstr)):            
            self.summaryOutput = self.summarizer(self.fstr[i:i+3000], truncation = True, do_sample=False)
            ffile1.write(self.summaryOutput[0]['summary_text'])
            ffile1.write("\n")
            i = i+3000
        self.summaryOutput = self.summarizer(self.fstr[i:], truncation = True, do_sample=False)
        ffile1.write(self.summaryOutput[0]['summary_text'])
        ffile1.write("\n")
        ffile1.close()

if __name__ == "__main__":
    fName = "C://Users//kuppala2//Desktop//SWM//20news-18828.tar//20news-18828//20news-18828//cluster_20-20221121T214127Z-001/cluster_20"
    # fName = "C://Users//kuppala2//Desktop//SWM//folder"
    epoch_time = str(int(time.time()))
    outputFileName = "cluster20_output" + epoch_time
    summary = Summary(fName, outputFileName)
    summary.iterateFolder()

"""
Token indices sequence length is longer than the specified maximum sequence length for this model (2933 > 1024). 
Running this sequence through the model will result in indexing errors
"""
