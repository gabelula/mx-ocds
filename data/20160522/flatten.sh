#!/bin/python

echo 'CONVERTING OCDS FILES TO CSV'
echo '----------------------------'
for f in ./*.json
do
  echo 'Flattening $f now'
  flatten-tool flatten $(f) --main-sheet-name releases --output-name $(f)
done
