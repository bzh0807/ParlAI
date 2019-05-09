#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
'''
    Provides a dump of Wikipedia articles from 2/3/18.

    One can either load full articles, using 'wikipedia:full',
    or simply load the first paragraphs of the articles,
    using 'wikipedia:summary'

    To put the article in the labels and the title in the text, specify
    ':key-value' at the end (for a title/content key-value association)

'''
from parlai.core.teachers import DialogTeacher
from .build import build

import json
import os

class PubMedTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        #self.key_value = ':key-value' in opt['task']
        opt['task'] = 'pubmed_qa4p'
        build(opt)
        opt['datafile'] = os.path.join(opt['datapath'], 'pubmed_qa4p/pubmed_parlai_nonull.json')
        self.id = 'pubmed_qa4p'
        super().__init__(opt, shared)

    def setup_data(self, path):
        print('loading: ' + path)
        with open(path) as wf:
            for pubmed_json in wf:
                trial = json.loads(pubmed_json)
                title = trial['title']
                if not title or title == '':
                    title = 'no title'
                text = trial['text']
                tid = trial['id']
                #if self.key_value:
                #if text != 'N/A':
                #if not title:
                #    print('title inval')
                #    print(trial)
                #if not tid:
                #    print('id inval')
                yield (title+' '+tid, [text]), True
                #else:
                #    yield (title + '\n' + text, ['']), True

class DefaultTeacher(PubMedTeacher):
    pass
