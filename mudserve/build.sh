rm -rf ./mudrpc
thrift -r --gen py:new_style ./include.thrift
mv ./gen-py/mudrpc ./mudrpc
rm -rf ./gen-py
