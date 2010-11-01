rm -rf ./mudrpc
thrift -r --gen py:new_style main.thrift
mv gen-py mudrpc
