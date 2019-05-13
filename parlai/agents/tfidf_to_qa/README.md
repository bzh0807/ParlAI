# TFIDF Retriever to QA
 The *TFIDF Retriever* is an agent that constructs a [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
 matrix for all entries in a given task. It generates responses via
 returning the highest-scoring documents for a query. It uses a SQLite database
 for storing the sparse tfidf matrix, adapted from [here](http://github.com/facebookresearch/DrQA/).

 The QA Model used is currently also from DrQA, but can be modified to other models in the future.

 ## Environment Setup
 Everything runs in an anaconda virtualenv, so the first step is to setup a new virtualenv. Once setup, it can
 be used using something like the following:
 ```bash
 export PATH=/af5/wtz5pp/anaconda3/bin:$PATH
 source activate /af5/wtz5pp/anaconda3/envs/py3-drqa/
 ```
 The first line is not necessary if you set up everything so that the PATH automatically includes the anaconda bin.
 There are likely dependencies you will have to account for as well, but most should be accounted for in the
 requirements.txt file found in the repo.

 ## Files of Interest
 ```bash
 parlai/agents/tfidf_to_qa/tfidf_to_qa.py
 ```
 This file implements most of the system. It initalizes the TF-IDF rankers and passes the results to a QA model.
 Most changes to this file were to the __init__() and act() functions.

 ```bash
 parlai/agents/local_human_silent/local_human_silent.py
 ```
 This agent allows the passing of messages between the TF-IDF agent and QA agent. It is a modified version of the
 local_human agent used in the interactive.py example file.

 ```bash
 parlai/tasks/qa4patients
 parlai/tasks/pubmed_qa4p
 parlai/tasks/task_list.py
 ```
 These files constitute the dataset. The first one (which could have its name changed to clinical_qa4p) is for the
 ClinicalTrials dataset and the second one is for the PubMed dataset.
 The last one must be modified if any new tasks are created or if the tasks' names are changed. Changing a task name
 will also require a change to the TF-IDF dictionary creation invocations (next section).

 ## Script Invocations
 ```bash
 python examples/interactive.py -m tfidf_to_qa -mf data/models/tfidf_to_qa/pubmed_tfidf --extra-mf data/models/tfidf_to_qa/clinical_tfidf --retriever-num-retrieved 50
 ```
 This runs the main script which takes a question input and outputs an answer. -m is the model used, -mf is the main model file, --extra-mf specifies a comma-separated list of any additional model files that need to be used, --retriever-num-retrieved specifies how many documents to use from each dataset for the context.

 ```bash
 python examples/train_model.py -m tfidf_retriever -t pubmed_qa4p -mf data/models/tfidf_to_qa/pubmed_tfidf -dt train:ordered -eps 1
 python examples/train_model.py -m tfidf_retriever -t qa4patients -mf data/models/tfidf_to_qa/clinial_tfidf -dt train:ordered -eps 1
 ```
 Creates TF-IDF dictionaries for the specified tasks to be stored in the specified directory. This code also runs some training and validation steps which can be skipped over with Ctrl-C since there is no training necessary.


