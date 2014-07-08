#!bin/sh
cd /home/xinyuan/mysource/python/cola/process
mongoexport -d generic -c generic_example   -f title,content,url -o generic.cvs -q '{"content":{"$not":{$eq:null}}}'
cat generic.cvs|python trimhtml.py > generic.cvs.raw
cp generic.cvs.raw ../../wordseg-ex-utf8/
cd /home/xinyuan/mysource/python/wordseg-ex-utf8
cat generic.cvs.raw |python process.py > generic.cvs.raw.seged 
cp generic.cvs.raw.seged ../../ML/GibbsLDA++-0.2/models/casestudy/
cd /home/xinyuan/mysource/ML/GibbsLDA++-0.2
LINES=`wc -l models/casestudy/generic.cvs.raw.seged | cut -f1 -d' '`
sed -i "1i ${LINES}" models/casestudy/generic.cvs.raw.seged
#src/lda -est -alpha 0.5 -beta 0.1 -ntopics 100 -niters 100 -savestep 100  -twords 20 -dfile models/casestudy/generic.cvs.raw.seged

