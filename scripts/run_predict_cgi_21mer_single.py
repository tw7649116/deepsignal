# -*- coding: utf-8 -*-
'''
/*
 * @Author: huangneng 
 * @Date: 2018-10-26 15:27:23 
 * @Last Modified by: huangneng
 * @Last Modified time: 2018-10-28 11:19:16
 */
'''

import os

model_path = "/home/huangneng/master_deepsignal/deepsignal/last_v_models/cgi_21mer_single"
result_path = "/home/huangneng/master_deepsignal/deepsignal/last_v_results/cgi_21mer_single"
test_dir = "/home/huangneng/data/human_hx1.test.bn21.5xs/BJXWZ.x.hc_pos/ hx1.test.bn21.BJXWZ_C789101112D1E13.cgi.scgs"
model_name = '99'

test_path = '/home/huangneng/data/human_hx1.test.bn21.5xs/BJXWZ.x.hc_pos/ hx1.test.bn21.BJXWZ_C789101112D1E13.cgi.scgs'
out_name = result_path+'/result.txt'
# print(test_path)
# print(out_name)
cmd = "CUDA_VISIBLE_DEVICES=3 python ../predict.py -i {input}/ -o {model}/ -r {output} -n {modelname} -x 21 -y 512 -z 60 ".format(
    input=test_path, model=model_path, output=out_name, modelname=model_name)
print(cmd)
os.system(cmd)
