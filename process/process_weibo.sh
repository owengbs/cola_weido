cd /home/xinyuan/mysource/python/cola/process
mongoexport -d sina -c micro_blog   -f content -o weibo.cvs -q '{"content":{"$not":{$eq:null}}}'
cat weibo.cvs |python trimweibo.py  > weibo.cvs.raw
cp weibo.cvs.raw ../../wordseg-ex-utf8/
cd /home/xinyuan/mysource/python/wordseg-ex-utf8
cat weibo.cvs.raw |python process.py > weibo.cvs.raw.seged 
cp weibo.cvs.raw.seged ../../ML/GibbsLDA++-0.2/models/casestudy/
cd /home/xinyuan/mysource/ML/GibbsLDA++-0.2
src/lda -est -alpha 0.5 -beta 0.1 -ntopics 100 -niters 100 -savestep 100  -twords 20 -dfile models/casestudy/weibo.cvs.raw.seged
