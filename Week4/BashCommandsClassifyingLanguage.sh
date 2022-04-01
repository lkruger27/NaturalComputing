#!/bin/bash

# Languages, part 1
java -jar negsel2.jar -self english.train -n 10 -r 4 -c -l < english.test > ./ClassifyingLanguagesFiles/englishtest.txt
java -jar negsel2.jar -self english.train -n 10 -r 4 -c -l < tagalog.test > ./ClassifyingLanguagesFiles/tagalogtest.txt

# Languages, part 2
for idx in {1..9}
do
      # timing both commands as a rough estimate of repetoire size
    time (java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < english.test > ./ClassifyingLanguagesFiles/englishtest_r${idx}.txt ;
    java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < tagalog.test > ./ClassifyingLanguagesFiles/tagalogtest_r${idx}.txt)
done

# Languages, part 3
for idx in {3..4}
do
    java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < ./lang/plautdietsch.txt > ./ClassifyingLanguagesFiles/plautdietschtest${idx}.txt
    java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < ./lang/hiligaynon.txt > ./ClassifyingLanguagesFiles/hiligaynontest${idx}.txt
    java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < ./lang/middle-english.txt > ./ClassifyingLanguagesFiles/middleenglishtest${idx}.txt
    java -jar negsel2.jar -self english.train -n 10 -r $idx -c -l < ./lang/xhosa.txt > ./ClassifyingLanguagesFiles/xhosatest${idx}.txt
done
