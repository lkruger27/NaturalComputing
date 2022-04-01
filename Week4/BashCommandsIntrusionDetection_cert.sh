#!/bin/bash

# IntrutionDetection, part 2
for K in {5..7}  
do
    for r in {2..4}
    do
        for idx in {1..3}
        do
            java -jar negsel2.jar -alphabet file://snd-cert.alpha -self snd-cert-chunk${K}.train -n $K -r $r -c -l < snd-cert-chunka${K}.${idx}.test > test_cert${K}_${r}.${idx}.txt
        done
    done
done
