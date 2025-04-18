# TSE 2024 - Towards a Cognitive Model of Dynamic Debugging: Does Identifier Construction Matter?

## Purpose:
We provide the stimuli and processed behavioral data (dataset) of our journal article. Stimuli are seperated by problem per treatment. If you would like the raw behavioral data, fNIRS (brain imaging) raw data, or analysis scripts, please email Priscila Santiesteban (pasanti@umich.edu).

## Table of Contents:

- `/stimuli` : containts the Python probelms used for our experiment analysis. Numbers on file titles are associated with the Leetcode problem the solution was dervied by followed by the idenfier variable condition. "simple" corresponds to single-morpheme treatment, "complex" to multi-morpheme, "nonword" to psuedoword, and "original" to the unchanged varaible name.
- `/debugging-phases-data` : contains pre-processed data of the dynamic phases transitioned by each participant. These transitions were derived using behavioral markers such as time of keystroke, window-switching, etc. For scripts that derive this phases analysis, please email the authors.
- `/full-behavioral-data` : contains the CSV of all the behavioral data for each participant for each problem. This contains time (total and per debugging phase), keystroke behavior per problem, accuracy (numPass), reading ability scores, and other demographic information. For raw data, please contact the authors.


## Paper Summary:

Authors: Danniell Hu, Priscila Santiesteban, Madeline Endres, Westley Weimer

Published: IEEE Transactions on Software Engineering, 2024.

Presented: ICSE Journal First Track Ottawa, Canada, 2025.

Abstract: Debugging is a vital and time-consuming process in software engineering. Recently, researchers have begun using neuroimaging to understand the cognitive bases of programming tasks by measuring patterns of neural activity. While exciting, prior studies have only examined small sub-steps in isolation, such as comprehending a method without writing any code or writing a method from scratch without reading any already-existing code. We propose a simple multi-stage debugging model in which programmers transition between Task Comprehension, Fault Localization, Code Editing, Compiling, and Output Comprehension activities. We conduct a human study of n = 28 participants using a combination of functional near-infrared spectroscopy and standard coding measurements (e.g., time taken, tests passed, etc.). Critically, we find that our proposed debugging stages are both neurally and behaviorally distinct. To the best of our knowledge, this is the first neurally-justified cognitive model of debugging. At the same time, there is significant interest in understanding how programmers from different backgrounds, such as those grappling with challenges in English prose comprehension, are impacted by code features when debugging. We use our cognitive model of debugging to investigate the role of one such feature: identifier construction. Specifically, we investigate how features of identifier construction impact neural activity while debugging by participants with and without reading difficulties. While we find significant differences in cognitive load as a function of morphology and expertise, we do not find significant differences in end-to-end programming outcomes (e.g., time, correctness, etc.). This nuanced result suggests that prior findings on the cognitive importance of identifier naming in isolated sub-steps may not generalize to end-to-end debugging. Finally, in a result relevant to broadening participation in computing, we find no behavioral outcome differences for participants with reading difficulties.

