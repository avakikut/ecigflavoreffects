---
title: 'FlavorAnalysis_official'
output:
  html_document:
    keep_md: yes

---

Methods

_E-cigarette text corpus_

The texts analyzed in this study were collected as part of a larger research project assessing the effects of e-cigarette and tobacco media coverage on youth and young adult perceptions and behaviors (Gibson et al., 2019). This dataset included all texts related to e-cigarettes between 5/18/2014 and 12/31/2017 on Twitter and longform sources. Longform texts included transcripts from eight major broadcast news outlets (ABC, CBS, NBC, PBS, CNN, Fox, MSNBC, NPR) and articles from the Associated Press wire (AP), 50 major U.S. Newspapers, and over 100 websites popular with youth and young adults as ranked by Nielsen. Of this corpus, 24,341,610 tweets and 11,691 longform texts were coded as e-cigarette relevant using validated search terms (e.g. “vaping”, “e-cigarette”, “e-juice”). Table 1 summarizes the initial methods used to classify e-cigarette texts prior to this study.

Table 1. E-cigarette content data collection and validity measures (05/2014-12/2017
```{}
Frequency of each longform source type (part of Table 1)
Source          Frequency
Broadcast news  3.00%
AP              9.80%
Newspapers      34.8%
Websites        52.4%

Script: 2. ContentDescriptiveStats.Rmd

```

_Defining e-cigarette flavor content._

We defined any text or tweet as e-cigarette flavor-related if it included one or more of the following: mention of the taste of e-cigarettes (i.e. e-juice/vapor); mention of food, beverage, or candy to describe the scent of e-cigarettes (e.g. cotton candy smelling vape); or description of e-cigarettes using taste-related adjectives or adverbs (e.g. delicious). Terms that described specific ingredients in e-cigarettes (e.g. herb-infused), descriptions that did not specifically relate to taste (e.g. cherry wood vape pen), and mentions of non-e-cigarette product flavors (e.g. flavored cigarettes or cigars), did not qualify as e-cigarette flavor-related.

_Developing and validating search terms for Twitter._

We hand-coded a randomly-selected sample of 2458 e-cigarette-related tweets (Sample 1) and found that 4.3% (n=105) met the criteria for flavor-related content described above. Krippendorff’s Alpha for the reliability between two coders was .98 (Krippendorff, 2019). To develop a list of search terms that would match the results of hand coding, we used Microsoft Excel (2016)’s “find” function to identify all tweets in Sample 1 that included flavor (flavoring/flavors/flavored/etc.) and/or taste (tastes/tasting/tasted/etc.). After verifying that these e-cigarette tweets met the criteria for flavor-related content, we inspected all other Sample 1 tweets for mentions of flavored e-cigarettes. Based on flavor-relevant tweets that did not include the terms flavor or taste, we added new terms to our initial search list. These included specific flavors (e.g. strawberry, melon, ginseng) and adjectives (e.g. delicious). We then compared our search term with the hand coded ‘gold standard’. Precision for our final list of terms on Sample 1 was .94 (105/112 tweets including the search terms were about e-cigarette flavor) and recall was 1.0 (105/105 flavor-related tweets included these terms). We used this validated search term list to generate a script for automatic coding (using Python version 3.7). Next, we verified this Sample 1-generated script maintained validity with a fresh sample of randomly selected tweets (Sample 2; n=4738), using hand coding and the Linguistic Inquiry and Word Count (LIWC) system.

LIWC’s categories “perception” and “ingest” identify terms related to food, flavor, and scent (Pennebaker, Booth & Francis, 2007). Of the relevant terms added to taste and flavor in Sample 1, 90% were categorized by LIWC into these two categories. In addition to reading all Sample 2 tweets classified as flavor-related by the Sample 1-generated script, we read all Sample 2 tweets classified as ingest or perception by LIWC to locate any flavor-relevant tweets missed by the script. We then compared the automatic coding of Sample 2 (using the Sample 1-generated script) with the LIWC + hand coding results. The previously developed script achieved .77 recall and .95 precision for Sample 2. Following these validation steps, we used the same script to automatically code all e-cigarette related tweets in our dataset for flavor-specific coverage.

```{}
Script for coding Twitter content: 1a. Twitter_regex_coding_fromCSV_taste.py
```

_Validating search terms for longform texts._

Using a script with the same flavor-related search terms generated for Twitter, we automatically coded a randomly selected sample of 200 e-cigarette-related longform texts (Sample 3). To improve accuracy and decrease noise, we applied a text “window” within +/-20 words of an e-cigarette related term. We increased precision on Sample 3 from .74 (using just search terms) to .90 (using search terms within the +/- 20 word window). The recall for both cases was 1.0, as we found no missed flavor-related texts. Inter-coder reliability for two coders was .94 (Krippendorff, 2019). Based on these validation measures, we ran the script with the window function on the entire set of e-cigarette related longform texts.

```{}
Script for coding longform content: 1b. Ava_WINDOWLongFormTasteScript_ALL_06.24.19.py
```

_Recent daily e-cigarette flavor coverage measure._

We measured “recent” media coverage for each survey respondent as the average number of daily tweets/texts on Twitter and longform sources pertaining to flavored e-cigarettes in the 28 days prior to taking the survey. To generate this measure, we separately summed the total number of flavor-related tweets and the number of longform texts for each day and then calculated the average daily volume for each source category in the 28 days before each survey date. We then standardized past-28 day counts for Twitter and longform separately.

```{}
Script for 28-day content measure: 3. TasteContentAggregating.r
Script for merging 28-day content measures with survey data: 4. Mergesurveycontentvariables.do
```

_Monthly-level reliability._

To be sure that assignment of flavor coverage scores for 28-day periods was reliable, we repeatedly estimated the level for random halves of content for each 28-day period and asked whether each half gave us a similar estimate. Specifically, we calculated the Spearman-Brown reliability coefficients for flavor-specific texts on Twitter and on Longform based on the average of 100 split-half correlations (Lance, Butts, & Michels, 2006; Nunnally, 1978). The median reliability was .99 for Twitter and .85 for longform, showing that estimates met criteria for reliability at the 28-day level.

```{}
Folders for split-half analyses: 5a. SpitlhalfTasteLF / 5b. SplithalfTasteTwitter
```

_Survey Data_

_Survey sample._

We used survey data from a nationally representative rolling cross-sectional survey of youth and young adults (ages 13-26). Respondents were first surveyed by phone from mid-June 2014—mid-June 2017 (n=11,847; response rate = 21%) and again six months later from mid-December 2014—mid-December 2017 (n=4470; follow up response rate 38%). This follow-up survey included measures of 14 beliefs about e-cigarettes and vaping on a 1-4 (strongly disagree to strongly agree) scale. Because e-cigarette taste perceptions were not measured in the first round of surveys, we used data exclusively from the second wave. Among other variables, age, sex, race, academic performance, respondent and parent education, respondent combustible cigarette use, and respondent e-cigarette use were collected. Sampling and weighting procedures to match the Current Population Survey distribution of important demographic variables were developed, and the survey was implemented by Social Science Research Solutions (SSRS). See Kranzler, Gibson, and Hornik (2017) for more information about survey procedures.

_Flavor perception measurement._
The primary outcome measure for this analysis was the belief that e-cigarettes taste good, as measured by endorsement of the statement: “If I vape or use e-cigarettes every day, I will enjoy the taste.” The four possible responses were: strongly agree = 4, agree = 3, disagree = 2, or strongly disagree = 1.

_Potential moderators._

We expected that any effects of media coverage on beliefs might be moderated by age or prior vaping experience; we thought that younger respondents might have fewer e-cigarette experienced peers who would directly communicate about vaping, making media sources more influential; similarly, youth with vaping experience might be less influenced by media information about flavors, given they had direct experience. We divided respondents into two groups—adolescents (13-17) and young adults (18-26), based primarily on differences in legal access to e-cigarettes. Another potential moderator is vaping experience. Respondents were asked “Have you ever tried vaping or using e-cigarettes, even one or two puffs?” Binary responses include yes (1) or no (0).

_Analysis_

We analyzed data with Stata version 13.1 (StataCorp, 2017). We used ordinal logistic regression clustered by date, to account for the fact that all respondents interviewed on a specific date (on average 4) were assigned a common exposure score. Calculated standard errors were adjusted for the incorporation of weights. We standardized scores for past 28-day e-cigarette flavor-related media coverage on Twitter and on longform texts to allow easy comparability of their coefficients, and regressed main effects of coverage scores and their interaction on survey-reported beliefs that e-cigarettes taste good (agreement scale 1-4). For presentation purposes (Figure 1), we also used binary regression, dichotomizing agreement into 1=strongly agree/agree and 0=strongly disagree / disagree.

_Flavor Coverage Themes_

After testing our main hypothesis, we examined a small sample of randomly selected texts by hand to both verify that texts predominantly characterized e-cigarettes as good-tasting, as well as to describe the themes present within flavor-specific coverage. We developed a list of themes: promotions, policy, youth appeal, health risks, and normative descriptions. See Appendix B more information about these procedures and inclusion criteria for each theme.

Results

_Flavor Coverage Characteristics_ 

Our effects analyses below make the assumption that flavor specific coverage described e-cigarettes as good-tasting. Before presenting those effects results, we briefly describe the content of the coverage and confirm its positive tenor. In hand coding randomly selected samples of flavor-related tweets and texts (results presented in Table 2), we found no longform texts and a very small portion of tweets (1.7%; 95% CI, 0.00, 3.2%) portrayed e-cigarette flavor or taste negatively. This was true whether the overall valence of the text was positive or negative towards e-cigarette use. Most Twitter content pertaining to e-cigarette flavors was promotional (66%), and most longform texts (75%) discussed the youth appeal of flavors (49%), the health risks of flavorings (12%), and/or related policies (64%). Very few tweets mentioned health risks, youth appeal, or policies. About a quarter of texts from each source were normative descriptions that mentioned or implied use of flavored products but neither promoted products nor discussed their risks. Overall, flavor-specific coverage made up 4.4% of e-cigarette related tweets and 19.7% of total e-cigarette related longform texts over the period of content collection.

Table 2. E-Cigarette flavor content themes on Twitter and longform sources
```{}
Theme	                    Twitter Proportion (95% CI) (N=293)	       Longform Proportion (95% CI) (N=166)
Promotion	                 .66 (.61 - .71)	                           .03 (0.0 - .06)
Policy	                     .02 (.01 - .04)	                          .64 (.57 - .72)
Youth Appeal                  .02 (.01 - .04)	                          .52 (.44 - .59)
Health Risks	             .04 (.02 - .07)                              .21 (.15 - .27)
Normative Description	     .26 (.21 - .31)	                            .22 (.15 - .28)

Folder for flavor theme coding and reliability checks: TasteReliability check 
```


_Descriptive Statistics for Analysis_

We provide descriptive statistics for all measures in our analysis in Table 3. For the 28-day period before each survey date, the average flavor-related texts per day ranged from 0.5 to 5.9 for longform sources and 500 to 2500 for Twitter. The correlation between Twitter and longform flavor coverage, with day as the unit of analysis (n=1013), was not significant (.02; p=.20). Within the survey dataset, the final analysis includes all respondents who evaluated the statement that e-cigarettes taste good (n=4369). Overall, about half of respondents agreed or strongly agreed with this statement (49.9%).

Table 3. Univariate information for all variables (12/14/2014-12/17/2017)
```{}
Variable                                                	Average/Frequency

Content Measures	
Recent Daily E-Cigarette Flavor Longform Texts, M (SD)	    1.54 (0.88)
Recent Daily E-Cigarette Flavor Tweets, M (SD)	            798.00 (266.15)
	
Survey Measures 	
Agreement E-Cigarettes Taste Good (Scale 1-4), M (SD)	      2.44 (0.72)
1. Strongly Disagree (%)	                                   9.74
2. Disagree (%)	                                              40.17
3. Agree (%)                                                  46.02
4. Strongly Agree (%)	                                       4.07
	
Has Vaped (%)	                                              28.74
Adolescent (13-17 years old) (%)	                          55.51
Young adult (18-26 years old) (%)	                          44.49

Script: TasteanalysisScript.do
```

_Analysis_

We analyzed data with Stata version 13.1 (StataCorp, 2017). We used ordinal logistic regression clustered by date, to account for the fact that all respondents interviewed on a specific date (on average 4) were assigned a common exposure score. Calculated standard errors were adjusted for the incorporation of weights. We standardized scores for past 28-day e-cigarette flavor-related media coverage on Twitter and on longform texts to allow easy comparability of their coefficients, and regressed main effects of coverage scores and their interaction on survey-reported beliefs that e-cigarettes taste good (agreement scale 1-4). For presentation purposes (Figure 1), we also used binary regression, dichotomizing agreement into 1=strongly agree/agree and 0=strongly disagree / disagree.

Table 4. Ordinal logistic regression results: association between recent flavor coverage and strength of belief that e-cigarettes taste good (1-4 scale)a
```{}
Predictor	                     Main effects 	       Model with source interaction 
                                  OR	  95% CI	      OR   95% CI
Interview Date (from 1-1013)	  1.00	1.00, 1.00    	1.00	1.00, 1.00
Recent Longform E-cigarette 
Flavor Coverage (L)b           	  1.04	0.95, 1.13   	1.02	0.94, 1.11
Recent Twitter E-cigarette 
Flavor Coverage (T)b	          1.00	0.91, 1.09    	1.06	0.96, 1.16
Source Coverage Interaction 
(L X T)                                 	--	--    	1.21*	1.04, 1.41
Cut 1	                          2.25	-3.48, 7.97   	1.68	-4.04, 7.40
Cut 2	                          4.43 -1.29, 10.15	    3.87	-1.85, 9.58
Cut 3                              7.55	1.83, 13.28	    6.99	1.28, 12.71

Notes. N=4,369; *p<.05
a 1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Standardized past 28-day average

Script: TasteanalysisScript.do
```

Additional Analyses

_Periods of high coverage on both sources._
To illustrate cross-source interactive effects, we divided respondents into two categories: those with high (≥1/2 SD) recent longform coverage of e-cigarette flavor and those with average or lower ( 1/2 SD) recent coverage. The high coverage group included respondents with more than two average texts per day in the 28-days prior to survey date (x ̅=2.83; n=932). The lower coverage group included respondents with two or fewer past 28-day average texts per day (x ̅=1.18; n=3,437). Figure 1 shows the predicted probability of believing e-cigarettes taste good (agree/strongly agree) as Twitter coverage increases for each long form coverage level. Higher Twitter coverage was associated with belief, but only when long form coverage was also higher. Predicted agreement that e-cigarettes taste good was 63.1% when content from both sources was high (≥1/2 SD for both sources) compared to 54.0% at mean content levels.

Figure 1. Ordinal logistic regression results: association between recent flavor coverage and strength of belief that e-cigarettes taste good (1-4 scale)
```{}
Script: TasteanalysisScript.do
```

_Sensitivity check 1. Effect of overall e-cigarette coverage on taste perception._

To establish that the observed effects were specific to flavor-specific coverage and not merely an artifact of overall e-cigarette coverage, we again used ordinal logistic regression clustered by date to assess the relationship between past 28-day overall e-cigarette coverage on the belief that e-cigarettes taste good. In both main and interaction models, we found no effects of Twitter, longform overall e-cigarette coverage or their interaction on this belief. We additionally verified that the results of our main analysis were consistent when controlling for overall e-cigarette coverage on both sources (inserted tables from Appendix D).

_Sensitivity check 2._

Effect of flavor-specific e-cigarette coverage on unrelated e-cigarette perceptions.
We also used ordinal logistic regression clustered by interview date to assess the relationship of past 28-day flavor-specific e-cigarette coverage on thirteen other perceptions of e-cigarettes assessed in the survey (e.g. “Vaping or using e-cigarettes can help people quit smoking tobacco cigarettes”). These analyses produced a total of 39 tests of effects – including main effects of Twitter and longform coverage and their interaction on each of the 13 beliefs, in parallel to the focused results in Table 4. Of these 39 effects tested, flavor-specific coverage produced only 3 significant effects, and none for interactions, about what one would expect by chance (See Appendix D).   

_APPENDICES_

Appendix A. Preliminary Analyses: Associations between belief, intention, and vaping behavior

We conducted two preliminary analyses to assess the influence of the belief that e-cigarettes taste good on vaping behavior in our survey dataset. We assessed both (1) the association between agreement that e-cigarettes taste good and intention to vape in the following six month and (2) the association between intention to vape at baseline and self-report of vaping behavior six months later. For both analyses, we ran one model testing for main effects and one controlling for vaping experience.

_Intention Measure_

We measured intention as any openness to vape in response to the survey question: “How likely is it that you will vape or use an e-cigarette, even one or two puffs, in the next six months?” Possible responses included: definitely will not, probably will not, probably will, definitely will, don’t know. We dichotomized responses, measuring intention as any response other than “definitely will not” (0 = definitely will not, 1= probably will not/probably will/definitely will/don’t know)

_Preliminary Analysis 1: Belief-Intention Relationship_

Controlling for vaping experience, we used logistic regression to measure the relationship between the belief e-cigarettes taste good (agreement scale 1-4) and odds of intending to vape. As with our main study, we used second-wave surveys from a larger dataset of rolling two-wave longitudinal surveys (taste perceptions were not measured at the first wave). Among all respondents interviewed in this second-wave, 28.4% had vaped before and 27.0% intended to vape in the next six months. Of respondents that had never vaped, 11.3% intended to try vaping in the next six months. As shown in Table A1, believing e-cigarettes taste good was significantly associated with intending to vape in the next six months. For respondents that had never vaped before, this belief more than doubled odds of intending to try vaping.

Table A1. Logistic regression results: Association between belief e-cigarettes taste good and odds of intending to vape
```{}
 
	                                  Main Effects Model          	          Controlling for Vaping Experience
	                                  
Predictor	                          Odds Ratio	95% CI                       Odds Ratio	  95% CI
Belief E-cigarettes Taste Gooda 	  3.24***   	2.74, 3.83                  	2.33***	    1.95, 2.78
Vaping Experience 
(Has Vaped at T2)b                  	-         -	                              6.94***	  5.57, 8.65
Constant	                          0.02***	    0.01, 0.04	                  0.25***	    0.02, 0.04

Notes. N=4,369; Survey measures reflect population weighting; *p<.05, **p<.01 ***p<.001
a 1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Baseline group is respondents who have never tried e-cigarettes or other vaping products at T2. 

Script: TasteanalysisScript.do

````

_Preliminary Analysis 2: Intention-Behavior Relationship_

For the second preliminary analysis, we included measurements from both waves in our larger survey dataset. Controlling for vaping experience, we used logistic regression to measure the association between intention to vape measured at initial surveys (T1) and vaping behavior measured at six-month follow up (T2). At T1, 23.5% of respondents had vaped before and 24.3% intended to vape in the next six months. Of respondents who had never vaped at T1, 11.6% intended to try vaping and 4.2% reported initiating vaping between T1 and T2. As shown in Table A2, intention to vape at T1 was significantly associated with vaping behavior at T2. Among respondents that had never vaped at T1, intending to vape more than tripled odds of initiating vaping in the next six months.

Table A2. Logistic regression results: Association between intention to vape (T1) and vaping behavior six months later (T2) 
```{}
	                                               Main Effects Model	        Controlling for Vaping Experience
	                                               
Predictor	                                        Odds Ratio  95% CI	                    Odds Ratio	95% CI
Intention to Vape (T1) 	                           10.48***   8.49, 12.94	                3.32***	     2.50, 4.41
Vaping Experience (Has Vaped at T1)a  	            -          -	                        40.25***	 26.99, 48.05
Constant	                                          0.28***   0.25, 0.31                 	0.12***	     0.10, 0.14

Notes. N=4,394; Survey measures reflect population weighting; *p<.05, **p<.01 ***p<.001
a Baseline group is respondents who have never tried e-cigarettes or other vaping products at T1. 

Script: TasteanalysisScript.do
```

Appendix B. Coding Flavor Coverage Themes

To define flavor coverage themes, we first hand coded a randomly generated sample of flavor-related tweets (n=100) and longform texts (n=37). We noted the subject of each flavored e-cigarette mention and then later categorized these subjects into five themes. Using proportions of texts/tweets in each theme for these initial samples, we estimated that new sample sizes of 150-300 would provide narrow enough confidence intervals (p ̂±z*  √( p ̂(1-p ̂ ) )/n) to show differences in proportions between longform and Twitter. We pulled a second random sample of 200 longform texts and 300 tweets. Our final coded sample excluded duplicates and texts miscoded for flavor (293 tweets and 166 longform texts). In addition to themes, we made note of any text that stated or implied e-cigarettes (and/or certain flavors) were not appealing. Our final list of themes and inclusion criteria are defined below, with examples in Tables B1 and B2.

   _Promotion_: Text/tweet included descriptions of sales, discounts, coupons, and/or free trials promoting the purchasing                of e-cigarettes and/or e-cigarette accessories, information about where to buy e-cigarettes online (including               URLs to e-cigarette company pages), and reviews of e-cigarettes.
   
   _Policy_: Text/tweet was not promotional and mentioned flavors in the context of (existing or potential) legal                       regulations of e-cigarettes.
  
  _Youth appeal_: Text/tweet was not promotional and mentioned the attractiveness of flavored e-cigarettes products for
	           children, adolescents, minors, young adults, teens, or kids. Mentions of aspects of e-cigarettes that appeal                to youth other than flavor did not qualify for this category.
	           
  _Health risks_: Text/tweet was not promotional and provided information or statements about the harmfulness of chemicals                used to make e-cigarette flavorings. Mentions of health risks unrelated to flavoring chemicals did not                      quality for this category.
  _Normative description_: Text/tweet was not promotional and mentioned the use of flavored e-cigarettes without discussing               their health risks, youth appeal, or related policies.

Table B1. Example e-cigarette flavor tweets and themes

Table B2. Example e-cigarette flavor longform texts and themes

Appendix C. Regression Models Including Potential Moderators

Table C1. Ordinal logistic regression results: association of recent flavor coverage on strength of belief that e-cigarettes taste good (1-4 scale)a testing for effects of vaping experience  
```{}
Predictor	                       Model 1          	      Model 2         	                Model 3
	                                 OR  	95% CI	          OR	95% CI                      OR	95% CI
Date	                             1.00  1.00, 1.00          1.00	1.00, 1.00	           1.00 	1.00, 1.00
Longform Flavor Coverage (L)b	     1.02	0.94, 1.11        1.03	0.95, 1.12             1.03	    0.95 1.12
Twitter Flavor Coverage (T)b          1.06	0.96, 1.16	      1.04	0.94, 1.15             1.04 	0.94, 1.15
LXT 	                             1.21*	1.04, 1.41	      1.27** 1.08, 1.49	           1.27*	1.03, 1.56
Vaping Experience c                   -	  -	                   5.77*** 4.74, 7.02	       5.77***	4.74, 7.02
LXT Vaping Experience                 -   -                   -    -                        1.00    0.73, 1.35
Cut 1	                             1.68	-4.04, 7.40	      -0.28	-6.15, 5.58	            -0.29	-6.15, 5.58
Cut 2	                             3.87	-1.85, 9.58	       2.10	-3.76, 7.97	            2.10	-3.76, 7.96
Cut 3	                             6.99	1.28, 12.71	      5.62	-0.25, 11.48	        5.61	-0.25, 11.48

Notes. N=4,369; Survey measures reflect population weighting; *p<.05, **p<.01 ***p<.001
a1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Standardized past 28-day average
c Baseline group is respondents who have never tried e-cigarettes or other vaping products. 

Script: TasteanalysisScript.do
```

Table C2. Ordinal logistic regression results: association of recent flavor coverage on strength of belief that e-cigarettes taste good (1-4 scale)a testing for effects of age group 
```{}

Predictor	                        Model 1 	                Model 2                   Model 3
	                               OR  	95% CI	              OR	95% CI              OR	  95% CI
Date	                           1.00  1.00, 1.00           1.00	1.00, 1.00	    1.00	1.00, 1.00
Longform Flavor Coverage (L)b	   1.02	0.94, 1.11	          1.06	0.94, 1.11	    1.02	0.94, 1.11
Twitter Flavor Coverage (T)b	   1.06	0.96, 1.16	          1.02	0.97, 1.16      1.05	0.96, 1.15
LXT 	                           1.21*	1.04, 1.41	      1.19*	1.03, 1.38	    1.07	  0.88, 1.30
Young Adult (18-26 years)c 	          -   	-	              2.00***1.73, 2.32	    1.99***	.1.71, 2.30
LXT X Young Adult	                  -	    -	                    -	    -	    1.17	0.91, 1.51
Cut 1	                            1.68 -4.04, 7.40	      2.29	-3.41, 7.98	    2.15	-3.56, 7.85
Cut 2	                            3.87 -1.85, 9.58	      4.51	-1.18, 10.21	4.38	-1.32, 10.08
Cut 3	                            6.99 1.28, 12.71	      7.69	2.00, 13.38	    7.55	1.85, 13.26

Notes. N=4,369; Survey measures reflect population weighting; *p<.05, **p<.01 ***p<.001
a1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Standardized past 28-day average
c Baseline group is youth (13-17 years)

Script: TasteanalysisScript.do
```

Appendix D. Sensitivity Analyses: Isolating the effects of flavor coverage on flavor beliefs

_Sensitivity check 1. Effect of overall e-cigarette coverage on taste perception._

Table D1. Ordinal logistic regression results: association of overall recent e-cigarette coverage on strength of belief that e-cigarettes taste good (1-4 scale)a
 
```{}
                                                          Main effects 	         Model with source interaction 
                                                           OR	  95% CI	           OR  95% CI
Interview Date (from 1-1013)                            	1.00	1.00, 1.00	        1.00	1.00, 1.00
Recent Overall Longform E-cigarette Coverage (L)b	        1.01	0.93, 1.10        	1.01	0.92, 1.10
Recent Overall Twitter E-cigarette Coverage (T) b	        1.02	0.93, 1.11	        1.01	0.92, 1.11
Source Coverage Interaction (L X T)	                         -	    -	                1.01	0.92, 1.10
Cut 1	                                                    1.86	-4.09, 7.81	        1.63	-4.61, 7.86
Cut 2	                                                    4.04  -1.91, 9.98        	3.80	-2.43, 10.04
Cut 3	                                                    7.15	1.21, 13.09	        6.92	0.69, 13.15

Notes. N=4,369; *p<.05, **p<.01 ***p<.001
a 1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Standardized past 28-day average

script: TasteanalysisScript.do

```

Table D2. Ordinal logistic regression results: association of recent e-cigarette flavor coverage on strength of belief that e-cigarettes taste good (1-4 scale)a controlling for overall e-cigarette coverage
```{}

Predictor	                                                 Main effects 	        Model with source interaction 
                                                           OR	  95% CI	          OR  95% CI
Interview Date (from 1-1013)	                            1.00	1.00, 1.00	      1.00	1.00, 1.00
Recent Longform E-cigarette Flavor Coverage (L) b	        1.05	0.95, 1.13	      1.04	0.94, 1.11
Recent Twitter E-cigarette Flavor Coverage (T) b	        1.00	0.91, 1.09        1.00	0.96, 1.16
Recent Overall Longform E-Cigarette Coverage b	           0.97   0.87, 1.18	     0.97	0.87, 1.09
Recent Overall Twitter E-Cigarette Coverage b	            1.04	0.92, 1.18    	  1.01	0.89, 1.14
LXT	                                                          -	    -	              1.21*	1.04, 1.41
Cut 1	                                                    2.39	-3.66, 8.43	      1.68	-4.04, 7.40
Cut 2	                                                    4.47	-1.47, 10.61      3.87	-1.85, 9.58
Cut 3	                                                    7.69	1.65, 13.73       6.99	1.28, 12.71
Notes. N=4,369; *p<.05, **p<.01 ***p<.001
a 1=Disagree, 2=Disagree, 3=Agree, 4=Strongly Agree 
b Standardized past 28-day average

Script: TasteanalysisScript.do
```

_Sensitivity check 2._

Table D3. Ordinal logistic regression results for 13 e-cigarette beliefs unrelated to e-cigarette taste
```{}
Belief 	        Recent Twitter E-Cigarette Flavor Coverage (T)	Recent Longform E-Cigarette Flavor Coverage (L)	L X T
	                                              OR	95% CI	     OR	  95% CI	      OR	95% CI
…I will become addicted to nicotine.	         1.02	0.93, 1.12	1.10	1.00, 1.21	0.91	0.79, 1.05
…I will be controlled by vaping.            	 1.00	0.90, 1.11	1.06	0.95, 1,17	0.94	0.81, 1.10
…I will develop cancer.	                        1.00	0.91, 1.11	1.06	0.97, 1.15	0.89	0.77, 1.04
…I will develop headaches.	                     1.01	0.92, 1.11	1.02	0.93, 1.11	1.01	0.87, 1.17
…I will enjoy life more.                        0.90*	0.81, 0.99	1.07	0.97, 1.17	0.99	0.83, 1.17
…I will feel relaxed.	                         0.96	0.88, 1.05	1.07	0.98, 1.16	1.00	0.86, 1.17
…I will get wrinkles.		                     1.09*	1.00, 1.20	0.98	0.89, 1.08	0.98	0.85, 1.13
…I will look uncool.                             1.05	0.96, 1.15	1.01	0.93, 1.10	1.05	0.90, 1.22
…I will lose my teeth.                           1.02	0.94, 1.11	1.03	0.96, 1.11	0.88	0.77, 1.00
…It will be less harmful to me 
than if I smoke tobacco cigarettes.	             0.98	0.90, 1.07	0.99	0.91, 1.09	1.00	0.87, 1.15
Breathing vapor from other people’s 
e-cigarettes or vape pens harms you.a
                                            	   0.98	0.91, 1.05	1.00	0.91, 1.10	0.94	0.83, 1.05
Peer norms (Response to: How many 
people your age would you guess 
vape or use e-cigarettes?)b
	                                              1.15**	1.05, 1.27	0.98	0.90, 1.06	1.15	0.98, 1.34

Vaping or using e-cigarettes can
help people quit smoking tobacco cigarettes. 
                                              	1.03	0.95, 1.12	0.98	0.89, 1.08	1.03	0.89, 1.20
                                            	
Notes. N=4,369; *p<.05, **p<.01 ***p<.001; All belief items beginning with ellipses were preceded by “If I vape or use e-cigarettes every a day…” Unless otherwise indicated, responses options were 1= Strongly disagree, 2= Disagree, 3= Agree, 4= Strongly agree. 
aThe response options for this item were: 1= Not at all, 2= A little, 3= Somewhat, 4= A lot  
bThe response options for this item were: 1= None, 2= A few, 3= About half, 4= Most 


Three belief items were significantly associated with flavor-specific Twitter coverage. When controlling for overall e-cigarette coverage, only one belief item remained significantly associated with flavor-specific coverage (…I will enjoy life more; OR=0.85; CI, 0.74- 0.98).  The two other belief items (…I will get wrinkles and peer norms) were not significantly associated with flavor-specific Twitter coverage when controlling for overall e-cigarette coverage (respectively: OR=1.04; CI, 0.92-1.18 and OR=1.06; CI, 0.93-1.21).

Script: TasteanalysisScript.do

```



