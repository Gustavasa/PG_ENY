# Fetch a sample corpus
mkdir data
mkdir data/samples
curl http://norvig.com/big.txt -o data/samples/big.txt

# Generate stats using NSP
mkdir data/output
cd scripts
./generate_stats.sh ../data/samples/big.txt ../data/output/

# Create binary dictionaries
cd ..
mkdir dictionaries
mkdir dictionaries/test
cd scripts
python makedict.py -u ../data/output/unigrams.txt -n ../data/output/ngrams2.ll,../data/output/ngrams3.ll,../data/output/ngrams4.ll -o ../dictionaries/test/big.dict

# Create binary dictionaries for unit tests
python makedict.py -t
python unittests.py
cd ../cpp
make test
