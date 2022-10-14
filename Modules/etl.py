import pdfplumber 
import re
from collections import Counter
import nltk
import pandas as pd
from os import listdir
import plotly.express as px
import streamlit as st

nltk.download('stopwords')

stopwords = nltk.corpus.stopwords.words('portuguese')

def list_files(path=None):
    files_list = [arq for arq in listdir(path)]
    return files_list

class government_plans:
    def __init__(self, filepath):
        self.filepath = filepath

    def extract_first_page(self):
        pdf = pdfplumber.open(self.filepath)
        page = pdf.pages[0]
        text = page.extract_text()

        print(f'First page data\n {text}')

        pdf.close()

    def extract_whole_text(self):
        pdf = pdfplumber.open(self.filepath)
        final = ''
        n_pages = len(pdf.pages)

        for page in range(n_pages):
            data = pdf.pages[page].extract_text()
            final = final + '\n' + data

        return final

    def formating(self):
        final = self.extract_whole_text()
        final_lower = final.lower() 
        
        all_words = re.sub(r'[^\w\s]',' ', final_lower)

        return all_words

    def tokenizer(self):
        all_words = self.formating()
        all_words_tokens = re.findall(r'\w+',all_words)

        return all_words_tokens

    def clean_stopwords(self):
        words_tokens = self.tokenizer()
        words_no_stopwords = []
        
        for word in words_tokens:
            if (word not in stopwords) & (len(word)>1):
                words_no_stopwords.append(word)

        return words_no_stopwords

    def word_counter(self):
        words_no_stopwords = self.clean_stopwords()
        word_counter = Counter(words_no_stopwords)
        word_counter = word_counter.most_common(30)
        return word_counter

    def convert_to_dataframe(self):
        word_counter = self.word_counter()
        dataframe = pd.DataFrame(word_counter, columns=['Word','Quantity'])
        return dataframe

    def wc(self):
        words_no_stopwords = self.clean_stopwords()
        all_words = " ".join(s for s in words_no_stopwords)
        return all_words

    def final(self):
        final_result = self.convert_to_dataframe()
        return final_result

class execute:
    def __init__(self, folderpath):
        self.folderpath = folderpath

    def DC(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_DC.pdf':
                    dc = government_plans(path+'/'+item)
                    plan_dc = dc.final()
                    all_words_dc = dc.wc()
                    return plan_dc, all_words_dc
    
    def MDB(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_MDB.pdf':
                    mdb = government_plans(path+'/'+item)
                    plan_mdb = mdb.final()
                    all_words_mdb = mdb.wc()
                    return plan_mdb, all_words_mdb
    
    def NOVO(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_NOVO.pdf':
                    novo = government_plans(path+'/'+item)
                    plan_novo = novo.final()
                    all_words_novo = novo.wc()
                    return plan_novo, all_words_novo
    
    def PCB(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PCB.pdf':
                    pcb = government_plans(path+'/'+item)
                    plan_pcb = pcb.final()
                    all_words_pcb = pcb.wc()
                    return plan_pcb, all_words_pcb
    
    def PDT(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PDT.pdf':
                    pdt = government_plans(path+'/'+item)
                    plan_pdt = pdt.final()
                    all_words_pdt = pdt.wc()
                    return plan_pdt, all_words_pdt

    def PL(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PL.pdf':
                    pl = government_plans(path+'/'+item)
                    plan_pl = pl.final()
                    all_words_pl = pl.wc()
                    return plan_pl, all_words_pl
    
    def PROS(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PROS.pdf':
                    pros = government_plans(path+'/'+item)
                    plan_pros = pros.final()
                    all_words_pros = pros.wc()
                    return plan_pros, all_words_pros

    def PSTU(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PSTU.pdf':
                    pstu = government_plans(path+'/'+item)
                    plan_pstu = pstu.final()
                    all_words_pstu = pstu.wc()
                    return plan_pstu, all_words_pstu

    def PT(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PT.pdf':
                    pt = government_plans(path+'/'+item)
                    plan_pt = pt.final()
                    all_words_pt = pt.wc()
                    return plan_pt, all_words_pt

    def PTB(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PTB.pdf':
                    ptb = government_plans(path+'/'+item)
                    plan_ptb = ptb.final()
                    all_words_ptb = ptb.wc()
                    return plan_ptb, all_words_ptb
    
    def PUP(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_PUP.pdf':
                    pup = government_plans(path+'/'+item)
                    plan_pup = pup.final()
                    all_words_pup = pup.wc()
                    return plan_pup, all_words_pup
    
    def UNIAOBR(self):
        path = self.folderpath
        files = list_files(path+'/')
        for item in files:
            regex =  r'^\w+.[pdf]{1,3}'
            if (re.search(regex, item)):
                if item == 'Plano_UNIAOBR.pdf':
                    uniaobr = government_plans(path+'/'+item)
                    plan_uniaobr = uniaobr.final()
                    all_words_uniaobr = uniaobr.wc()
                    return plan_uniaobr, all_words_uniaobr

run = execute('Planos de Governo')

plan_dc, all_words_dc = run.DC()
plan_mdb, all_words_mdb = run.MDB()
plan_novo, all_words_novo = run.NOVO()
plan_pcb, all_words_pcb = run.PCB()
plan_pdt, all_words_pdt = run.PDT()
plan_pl, all_words_pl = run.PL()
plan_pros, all_words_pros = run.PROS()
plan_pstu, all_words_pstu = run.PSTU()
plan_pt, all_words_pt = run.PT()
plan_ptb, all_words_ptb = run.PTB()
plan_pup, all_words_pup = run.PUP()
plan_uniaobr, all_words_uniaobr = run.UNIAOBR()

