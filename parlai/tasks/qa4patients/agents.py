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

class TrialTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        #self.key_value = ':key-value' in opt['task']
        opt['task'] = 'qa4patients'
        build(opt)
        opt['datafile'] = os.path.join(opt['datapath'], 'qa4patients/clinical_parlai.json')
        self.id = 'qa4patients'
        super().__init__(opt, shared)

    def setup_data(self, path):
        print('loading: ' + path)
        with open(path) as wf:
            for trial_json in wf:
                trial = json.loads(trial_json)
                title = trial['title']
                text = trial['text']
                #if self.key_value:
                yield (title, [text]), True
                #else:
                #    yield (title + '\n' + text, ['']), True

class DefaultTeacher(TrialTeacher):
    pass
