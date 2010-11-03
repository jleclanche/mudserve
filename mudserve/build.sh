rm -rf ./mudrpc
thrift -r --gen py:new_style ./include.thrift
mv ./gen-py/mudserve/mudrpc ./mudrpc
rm -rf ./gen-py
