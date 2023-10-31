#### Part 2: LLMs for Training Data Generation

Refer to Part 1 ('SILLM_assignment_1.1.md') for background on this assignemnt. You will generate a specific type of training data called Counterfactually Augmented Data (CAD). CADs are created by making minimal changes to existing training data in order to flip their labels.

Use the same LLM types you used for Part 1. 


**Step 1.** Use them to create CADs via LLM prompting. Use the exact same prompts in the paper. Try to get the models to make both positive and negative examples [2 points]


**Step 2.** Create your own classifier: use a simple non-deep learning version such as Logistic Regression or SVM and one sophisticated deep learning approach by fine-tuning transformer-based models like BERT, RoBERTa, or DistilBERT. The classifiers can be of three modes:



1. Not trained on any CAD (*OG*) [0.5 points]
2. Trained on 50% original and 50% manual CADs that you get from the corresponding dataset (*mCAD*) (see Table 3 in the paper) [0.5 points]
3. Trained on 50% original and 50% automated CADs that you get from Step 1, one model for each type of CAD (e.g., *aCAD_GPT* and *aCAD_Flan*) [1 point]

**Step 3.** Use the classifiers trained in Step 2 to label the OOD datasets [2 points]


**Step 4.** Generate non-CAD data, examples similar to the existing training data, but the label is not flipped. Train the machine learning models on this data as well, and compare against OG, mCAD, and aCAD models. [Bonus: 2 points]

Answer the following questions:



1. Do your results for Step 3 have the same performance as those reported in the paper (figure 1)? [1 point]
2. How do your classifiers compare against direct labeling via LLMs (from part 1) [1 point]
3. Quantitatively analyze the automated CADs — how many of them are guardrail responses from the LLMs? [1 point]
4. If you remove these examples from the training data of the aCAD models, does performance improve? [1 point]