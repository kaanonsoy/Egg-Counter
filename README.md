# Egg-Counter

This project is to detect eggs using opencv library and color filter.

<img src="https://github.com/kaanonsoy/Egg-Counter/blob/main/example1.png" >

<img src="https://github.com/kaanonsoy/Egg-Counter/blob/main/example2.png" >

## Description
I divided the section where the code focuses on 14 columns and created a middle line so that the eggs could be counted more easily. This way, I obtained 28 sections. The code checks the sections before and after the middle line. If the egg appears in the sections before and after the middle line of the same column, it is added to the egg counter.

I also had to use a color filter because the eggs in the video I used were brown. You can adjust the code according to the color of the eggs you will count.
