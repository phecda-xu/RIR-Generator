#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import json


class AudioProcessor(object):
    def __init__(self, train_json, test_json, dev_json):
        self.train_json = train_json
        self.test_json = test_json
        self.dev_json = dev_json
        self.data_index = {}
        self.prepare_data_index()

    def addJson(self, json_file, mode):
        if mode is 'train':
            train_bg_pos_manifest = self.json2manifest(json_file)
            self.data_index['train_pos'].extend(train_bg_pos_manifest)
        if mode is "test":
            test_bg_pos_manifest = self.json2manifest(json_file)
            self.data_index['test_pos'].extend(test_bg_pos_manifest)
        if mode is "dev":
            dev_bg_pos_manifest = self.json2manifest(json_file)
            self.data_index['dev_pos'].extend(dev_bg_pos_manifest)

    def json2manifest(self, json_file):
        with open(json_file, "r") as f:
            load_dict = json.load(f)
        return load_dict

    def json2df(self, json_file):
        with open(json_file, "r") as f:
            load_dict = json.dumps(json.load(f))
        df = pd.read_json(load_dict, orient='records')
        return df

    def prepare_data_index(self):
        # pos & neg manifest
        train_df = self.json2df(self.train_json)
        train_pos_df = train_df[train_df['is_hotword']==1]
        train_neg_df = train_df[train_df['is_hotword']==0]
        self.data_index['train_pos'] = json.loads(train_pos_df.to_json(orient='records'))
        self.data_index['train_neg'] = json.loads(train_neg_df.to_json(orient='records'))
        test_df = self.json2df(self.test_json)
        test_pos_df = test_df[test_df['is_hotword']==1]
        test_neg_df = test_df[test_df['is_hotword']==0]
        self.data_index['test_pos'] = json.loads(test_pos_df.to_json(orient='records'))
        self.data_index['test_neg'] = json.loads(test_neg_df.to_json(orient='records'))
        dev_df = self.json2df(self.dev_json)
        dev_pos_df = dev_df[dev_df['is_hotword']==1]
        dev_neg_df = dev_df[dev_df['is_hotword']==0]
        self.data_index['dev_pos'] = json.loads(dev_pos_df.to_json(orient='records'))
        self.data_index['dev_neg'] = json.loads(dev_neg_df.to_json(orient='records'))

