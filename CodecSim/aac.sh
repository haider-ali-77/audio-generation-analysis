echo "----AAC----"
cd src 
tar xzvf libaacplus-2.0.2.tar.gz
cd libaacplus-2.0.2
./autogen.sh --enable-shared --enable-static

make
sudo make install
cd ../
