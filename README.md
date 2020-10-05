Experiments for EMNLP_2020 paper

#### Datasets summary
 
| Dataset  | #docs | top terms (coef>=1) | #matched sentences for top terms | placebo terms | #matched sentences for placebo terms |
| ---------| ------| --------------------| ---------------------------------| --------------| -------------------------------------|
| IMDB | 10,662 | 366 | 8,882 | 626 (coef<=0.1) | 12,996 |
| Kindle | 20,233 (N, 10,161) (P, 10,072) | 270 | 24,882 | 569 (coef <=0.2) | 13,850|
| Toxic comment | 15,216 | 329 | 8,414 | 750 (coef<=0.1) | 30,454 |
| Toxic tweet | 6,774 | 341 (coef >=0.7) | 9,224 | 574 (coef<=0.2) | 5,457 |




#### Data structure (class Dataset):

- X, y, df (dataframe), vec (countvectorizer),  feats(features in vocabulary), moniker (nick name)
- top_features, top_feature_idx, placebo_features, placebo_feature_idx
- topwd_sentObj_list, placebowd_sentObj_list (list of **SentenceEdit** objects)
  - remove_wd 
  - context
  - original_sentence_idx
  - label
  - embedding (bert last four layers)
- topwd_sentObj_dict, placebowd_sentObj_dict (map from word to a list of SentenceEdit objects)
	
- **ites** (dataframe recording matched sentences)
  - term (the word being removed)
  - sentence_id (current sentence idx)
  - control_obj: the matched control SentenceEdit object
  - treat_obj: the matched treatment SentenceEdit object
  - similarity: cosine similarity between context of matched sentences
  - difference: embedding difference between treat context and control context
  - ite: treat_label - control_label 

- BAD_POS, BAD_NEG, ALL_BAD, DUMMY_TERM
	
- **term_df** (features for word classification)
  - term
  - ite_abs_avg / top_5 / top_5_by_sim
  - similarity_scaled_avg / top_5 / std / max 
  - closest_pos / neg_similarity_scaled
  - ite_weighted_scaled
  - ite_x_similarity_scaled / scaled_top_5
  - diff_mean / mean_vec / mean_abs
  - diff_min_mean, diff_max_mean, diff_max_mean_abs
  - top_diff_mean
  - coef
  - pca

