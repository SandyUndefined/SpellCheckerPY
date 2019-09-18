# Spell Checker  and Auto Correction
# To do
 * Fastest way to check spelling of sentence and provide with **_candidates_**
# Spelling Task
1. Spelling error detection.  
2. Spelling error correction.
 * Auto correct
 * Suggest the correction
 * Suggest lists
 
 # Types of spelling errors
 1.Non-word errors.   
 2.Real-word errors.
  * Typographical errors.
  * Cognitive errors.
  
 # Non-word spelling errors
  1. Non-word spelling error detection:
   * Any word not in a **_dictionary_** is an error. 
   * The larger the dictionary the better. 
 
 2. Non-word spelling error correction:  
  * Generate **_candidates:_** real words that are similar to error. 
  * Choose the one which is best:  
     * Shortest weighted edit distance.
     * Highest noisy channel probability.
     
  
  # Real word spelling errors
   1. For each word w, generate candidate set:   
   * Find candidate words with similar **_pronunciations._**
   * Find candidate words with similar **_spelling_**
   * Include w in candidate set.
   2. Choose best candidate  
   * Noisy Channel 
   * Classifier.
 
 
