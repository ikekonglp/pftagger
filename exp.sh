#!/bin/bash

# running the parser

./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_nns.predicted --logtostderr

./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_vbd.predicted --logtostderr

./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_mod_nn_nns --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_nns.predicted --logtostderr

./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_mod_nn_vbd --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_vbd.predicted --logtostderr

# evaluation commands

perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_nns.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_ori_nn_nns.report

perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_nns.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_mod_nn_nns.report

perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_vbd.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_ori_nn_vbd.report

perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_vbd.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_mod_nn_vbd.report