# NLP_Tools
Natural Language Processing (NLP)-related Python modules for collaborative text semantic network analysis 

This repository contains various NLP-related functions I wrote to assist in my semantic network analysis (https://github.com/vinay918/SemanticNetworkAnalysis) research project. The most useful function that it currently contains is the ShallowProcessN1 function. Given a body of text, it performs Shallow 1-gram NLP Processing to extract the context of a body of text by:
1. Converting string to lower case.
2. Removing stop words.
3. 1-gram tokenizing (tokenized by individual words).
4. Part of Speech (POS) tagging.
5. Retaining nouns and verbs.

UPDATE:
1. Now contains similarity function to compute symmetric similarity of two bodies of text (by extracting key-concepts)


(Within the context of my project, it is used to extract context from student writing to compare the similarity of pages in a network of pages and students, and to see its implication on the behavior of students with respect to the content of pages).
