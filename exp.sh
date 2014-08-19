#!/bin/bash

# running the parser

# ./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_nns.predicted --logtostderr

# ./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_vbd.predicted --logtostderr

# ./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_mod_nn_nns --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_nns.predicted --logtostderr

# ./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/home/lingpenk/parsing_friendly_tagger/data/dev_mod_nn_vbd --file_prediction=/home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_vbd.predicted --logtostderr

# evaluation commands

# perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_nns.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_ori_nn_nns.report

# perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_nns -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_nns.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_mod_nn_nns.report

# perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_ori_nn_vbd.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_ori_nn_vbd.report

# perl scripts/eval.pl -g /home/lingpenk/parsing_friendly_tagger/data/dev_ori_nn_vbd -s /home/lingpenk/parsing_friendly_tagger/data/result/dev_mod_nn_vbd.predicted >  /home/lingpenk/parsing_friendly_tagger/data/report/dev_mod_nn_vbd.report

# Generate Data
for i in {1..44}
do
	for j in {1..44}
	do
		if [ "$i" -ne "$j" ]; then
				python BuildCFMatrix.py /media/Data/PTB/PTB_330/dev /media/Data/parsing_friendly_tagger/data/source/ ${i} ${j} 
		fi
	done
done

cd /home/lingpenk/TBP/TurboParser/
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:`pwd;`/deps/local/lib:"

for i in {1..44}
do
	for j in {1..44}
	do
		if [ "$i" -ne "$j" ]; then
				./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/media/Data/parsing_friendly_tagger/data/source/ori_${i}_${j} --file_prediction=/media/Data/parsing_friendly_tagger/data/result/ori_${i}_${j}.predicted --logtostderr
				./TurboParser --test --evaluate --file_model=/media/Data/models/210basic_sd330 --file_test=/media/Data/parsing_friendly_tagger/data/source/mod_${i}_${j} --file_prediction=/media/Data/parsing_friendly_tagger/data/result/mod_${i}_${j}.predicted --logtostderr
				perl scripts/eval.pl -g /media/Data/parsing_friendly_tagger/data/source/ori_${i}_${j} -s /media/Data/parsing_friendly_tagger/data/result/ori_${i}_${j}.predicted >  /media/Data/parsing_friendly_tagger/data/report/ori_${i}_${j}.report
				perl scripts/eval.pl -g /media/Data/parsing_friendly_tagger/data/source/ori_${i}_${j} -s /media/Data/parsing_friendly_tagger/data/result/mod_${i}_${j}.predicted >  /media/Data/parsing_friendly_tagger/data/report/mod_${i}_${j}.report
		fi
	done
done
