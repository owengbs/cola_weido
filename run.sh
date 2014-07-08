rm -rf data/master/jobs/wikipedia_crawler/
rm -rf data/jobs/wiki/
rm -rf data/worker/jobs/wikipedia_crawler/
python bin/coca.py -m 127.0.1.1 -runLocalJob /home/xinyuan/mysource/python/cola/contrib/wiki

