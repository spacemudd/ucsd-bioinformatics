# Introduction

This repo contains all graded work done by me (Shafiq al-Shaar) for the course of "[Bioinformatics Specialization](https://www.coursera.org/specializations/bioinformatics)" given by University of California San Diego.

# Tools used

1. Python3 - language used in implementing the course work / code challenges.

2. Sublime - text editor.

2. OneNote - for note taking.

3. AnkiApp - for creating flash cards.

4. OriFinder - http://tubic.tju.edu.cn/Ori-Finder/

# Work

## Week 1 - Finding Hidden Messages in DNA (Bioinformatics I)

### `genome_pattern.py`

![Running genome_pattern.py](https://github.com/spacemudd/ucsd-bioinformatics/blob/master/genome_pattern.png)

#### Hurdles

##### I wasn't able to get correct answer on large datasets as I pasted the dataset through the terminal.

	I got 117 because I copy-pasted the input from the browser into terminal, and there is a limitation on how many bytes (4096) can be read in one line from the terminal. If instead I run the program like:

		`xclip -o | python3 pattern_count.py`

	Then I get the correct answer.
	I copy-pasted the input, because the format of the extra dataset is different from the input of actual test sets, which is very unfortunate and should be changed. If I download the extra dataset instead, I need to delete the first line and strip carriage returns. But there's no such need with data challenge test sets.

See: https://stepik.org/lesson/2/step/7?discussion=291620&reply=291822&unit=8231 by `Arkadiusz Olek`

Which made me just load the file instead of pasting it.

### `frequent_words.py`

![Running frequent_words.py](https://github.com/spacemudd/ucsd-bioinformatics/blob/master/frequent_words.png)

#### Hurdles

##### A bit complicated.

The psuedocode may throw you off a little bit so you're better about reading over the problem again and the comments to get a better undestanding of the situation.

### `reverse_complement.py`

![Running reverse_complement.py](https://github.com/spacemudd/ucsd-bioinformatics/blob/master/reverse_complement.png)

### `pattern_occurence.py`

![Running pattern_occurence.py](https://github.com/spacemudd/ucsd-bioinformatics/blob/master/pattern_occurence.png)

### `computing_frequencies.py`

- `test_computing_frequencies.py`
- `computing_frequencies.py`

### `pattern_to_number.py`

- `test_pattern_to_number.py`
- `pattern_to_number.py`

---

# My background

1. My qualifications are 6 IGCSEs and TOEFL.

2. Couldn't continue A-Levels / University due the responsbility of taking care of my siblings.

3. I'm an IT software developer having done pretty large projects.

4. I was always fascinated of the bioinformatics realm since I first heared of it in 2012 on Reddit.

5. I'm hoping to go back to university after taking the Bioinformatics Specialization course.

# About me

I'm Shafiq, born in 1994 and been a software developer since 2009.

You can reach me via Twitter [@spacemudd](https://twitter.com/spacemudd).

You can also find me on [LinkedIn at Shafiq al-Shaar](https://www.linkedin.com/in/shafiq-alshaar/).

And for any web dev related jobs, you can reach me on [Upwork](https://www.upwork.com/freelancers/~016a784ba169116514).
