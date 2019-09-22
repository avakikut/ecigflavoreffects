# E-Cigarette Flavor Content and Perceptions 
E-cigarette flavor project overview

## The purpose of this project is to code tweets and texts for content pertaining to e-cigarette flavor, and then assess the association between past 28-day flavor texts and survey-reported belief that e-cigarettes taste good.

## The final repo will contain the following scripts and datasets:
1.	Python coding of content
  1.1 Scripts (spyder/python)
    *Twitter_ecigtaste_script
    *Longform_ecigtastewindow_script
  1.2 Outputs
    *Twitter_ecigtaste_coded.csv
    *Longform_ecigtastewindow_coded.csv
2.	Aggregating content by survey data
  2.1 Scripts
   *ContentSurveyDataAggregated.md
  2.2 Outputs
    *ContentSurveyDataAggregated.csv
    *Clustered regression results
    *Graphs
        *Content over trime 
        *Beliefs over time
        *Predicted proportions 
        
3. Random Sampling of Text Files for Thematic coding on qualtrics
  3.1 Creating sample in r script: ContentDescriptiveStats.Rmd
    3.1a: Inputs
     *LFTasteCoded_final.csv (All coded longform articles but no content column)
     *ak_window_taste_longform_all_metadata.xlsx (all   articles with content columns)
     *ecig_no_duplicates_taste_final.csv (all tweets coded)
    3.1b: Outputs
      *LFTaste.csv (all ecig longform coded for taste)
      *LFTaste300.csv (random sample of longform coded for taste)
      *LFTaste300IDContent3.txt (random sample merged with ak_window_taste_longform_all_metadata.xlsx content columns)
      *TwitterTaste300.csv (random sample of 300 taste tweets)
       *TwitterTaste300IDContent.txt (Random Sample of 300 taste tweets with article content)
  3.2: Preparing samples in spyder scripts: ContentDescriptiveStats.RmdTwitterTaste300forQualtrics.py/LFTaste300forQualtrics.py
     3.2a: Inputs
       *LFTast300IDContent.txt/TwitterTast300IDContent.txt
    3.2b: Outputs
      *LFTaste300_formatted_for_Qualtrics.csv / TwitterTaste300_formatted_for_Qualtrics.csv (random samples with set columns)
   
    
    
    