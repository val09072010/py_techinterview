#!/bin/bash

cut -d '-' -f 1 access.test  | sort -n > sorted.test ; while true ; do ip1=`head -n 1 sorted.test` ; num=`grep $ip1 sorted.test | wc -l` ; echo $num $ip1 >> ips.map ; tail -n +$((num+1)) sorted.test > sorted.tmp ; if ! [ -s sorted.tmp ] ; then break ; else rm sorted.test ; mv sorted.tmp sorted.test ; fi ; done; rm -f sorted.tmp ; rm -f sorted.test ; sort -r -n ips.map | head -n 10 ; rm -f ips.map
