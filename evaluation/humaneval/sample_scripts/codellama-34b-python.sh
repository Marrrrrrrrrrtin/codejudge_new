python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 0 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 1 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 2 \
--temperature 0.4 \
--with_prefix \
--return_type "0_to_4_score_functional_correctness" \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 3 \
--temperature 0.4 \
--with_prefix \
--return_type "0_to_4_score_functional_correctness" \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 4 \
--temperature 0.4 \
--with_prefix \
--return_type "error_level" \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 1 \
--compare_prompt 5 \
--temperature 0.4 \
--with_prefix \
--return_type "error_level" \
--num_samples 3

python ./humaneval/code_score.py \
--test_case python-small-test \
--model CodeLlama-34b-Instruct \
--step 2 \
--compare_prompt 0 \
--analyze_prompt 0 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 3

cd /mnt/task_runtime/shiyl_workspace/workspace/code-judge/codejudge_new/evaluation
conda activate codejudge
python ./humaneval/code_score.py \
--test_case python-small-test \
--model Qwen \
--step 2 \
--compare_prompt 0 \
--analyze_prompt 0 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 1

cd /mnt/task_runtime/shiyl_workspace/workspace/code-judge/codejudge_new/evaluation
conda activate codejudge
CUDA_VISIBLE_DEVICES=3 python ./humaneval/code_score.py \
--test_case python-small-test \
--model Qwen \
--step 2 \
--compare_prompt 0 \
--analyze_prompt 0 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 1

cd /mnt/task_runtime/shiyl_workspace/workspace/code-judge/codejudge_new/evaluation
conda activate codejudge
CUDA_VISIBLE_DEVICES=0 python ./humaneval/code_score.py \
--test_case python-small-test \
--model Qwen \
--step 2 \
--compare_prompt 1 \
--analyze_prompt 0 \
--temperature 0.4 \
--with_prefix \
--return_type bool \
--num_samples 1