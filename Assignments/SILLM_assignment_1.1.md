### **Assignment 1:** Replicating And Building On ‘[People Make Better Edits: Measuring the Efficacy of LLM-Generated Counterfactually Augmented Data](https://indiiigo.github.io/files/Automated_CAD__emnlp23.pdf)’

**Deadline:** 06.12.2023

**What and how to submit:** as a jupyter notebook with all the results and the enriched datasets, i.e., the labels from all classification techniques (LLMs and the models you finetune) as separate columns. For example, your datasets should have columns like ‘chatgpt_run_1’, ‘\<open-source LLM\>_run_1’, ‘\<finetuned_model\>_run_1’, etc. You can submit the enriched dataset as a csv file or a pickle file. Please document all your design choices. You should add your name and matriculation number at the top of the notebook. Upload the notebook and enriched data to your private GitHub repository. 

**Disclaimer:** The datasets used in this assignment contain social media posts espousing sexist and hateful attitudes that may be distressing. Please take care in handling these datasets, especially when doing manual or qualitative analysis. Be sure to take enough breaks. If the contents of these datasets impede you from doing this assignment, please contact us to find alternatives. 

In this assignment, worth 20 points, you get to create different classifiers for detecting sexism OR hate speech, and ensuring that they are robust. The paper you will closely follow is available here: [https://indiiigo.github.io/files/Automated_CAD__emnlp23.pdf](https://indiiigo.github.io/files/Automated_CAD__emnlp23.pdf)

The assignment is divided into two parts, the first involves using LLMs for labeling (10 points + 2 bonus), while the second involves using them for creating training data (10 points + 2 bonus).

For both parts choose ONE construct – either sexism or hate speech, and for that particular construct, obtain or recreate 4 of the requisite **out-of-domain (OOD)** datasets (see Table 4 in the paper).


#### Part 1: LLMs for Labeling

We will use LLMs for labeling content and test 2 different experimental conditions:



1. **Examples** (3 conditions - no examples: zero-shot, some examples: few-shot, some positive and negative/counterexamples: counterexample)

    For the second mode ‘few-shot’, select between two and five examples from the dataset.


    For the third mode ‘counterexample’, manually produce new examples from existing ones. You should try to create **counterfactuals** or minimal counterexamples — these should be very close to the original example but have the opposite label. For instance:


    Original: Women shouldn’t be commentating on football matches


    Counterfactual: AI shouldn’t be commentating on football matches

2. **Definitions** (2 conditions - same definition across all datasets, varying definition across all datasets)

Use OpenAI’s API to access GPT3.5-turbo (i.e., ChatGPT) and an open-source model of your choice (e.g., Flan-T5, LlaMa) to label the datasets. For each model, you implement the following 6 modes:

**_A. few-shot, consistent definition:_** use the exact same prompt as the paper [0.5 points]

**_B. zero-shot, consistent definition:_** use the exact same prompt as the paper but without examples [0.5 points]

**_C. zero-shot, variable definition:_** vary the definition of the construct according to the specific paper the dataset came from, but zero-shot [0.5 points]

**_D. few-shot, variable definition:_** vary the definition of the construct according to the specific paper the dataset came from, but few-shot with examples from the specific datasets [0.5 points]

**_E. counterfactual, consistent definition:_** use the exact same prompt as the paper, but few-shot with examples from the specific datasets and counterfactual examples [Bonus +0.5 points]

**_F. counterfactual, variable definition:_** vary the definition of the construct according to the specific paper the dataset came from, but few-shot with examples from the specific datasets and counterfactual examples [Bonus +0.5 points]

In the end, you should compare the average performance (macro F1) of all of these different modes over at least 3 separate runs (to ensure robustness). 

Answer the following questions:



1. Do your results for mode A have the same performance as those reported in the paper (figure 1)? [2 points]
2. Is one of the LLMs better than the other one? [2 points]
3. Does varying the definition improve performance? [2 points]
4. Which prompting technique — zero-shot, few-shot — works best? [2 points] Bonus: also compare against counterfactual prompting [Bonus 1 point]

Part 2 can be found in the document 'SILLM_assignment_1.2.md'
