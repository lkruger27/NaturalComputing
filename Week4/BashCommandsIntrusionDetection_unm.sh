#!/bin/bash

# IntrutionDetection, part 4
for K in {5..7}  
do
    for r in {2..4}
    do
        for idx in {1..3}
        do
            java -jar negsel2.jar -alphabet file://snd-unm.alpha -self snd-unm-chunk${K}.train -n $K -r $r -c -l < snd-unm-chunka${K}.${idx}.test > test_unm${K}_${r}.${idx}.txt
        done
    done
done
