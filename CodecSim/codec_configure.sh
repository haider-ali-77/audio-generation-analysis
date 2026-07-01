echo "Configuring Required Codecs"

cd src
echo "----G722----"
cd src
unzip T-REC-G.191-201003-S\!\!SOFT-ZST-E.zip
cd Software/stl2009/g722
make -f makefile.unx

echo "----G728----"
			
cd ../g728/g728fixed
make -f makefile.unx

echo "----G726----"
cd ../../g726
make -f makefile.unx
      
echo "----G711----"
cd ../g711
make -f makefile.unx
      
cd ../../../

echo "----FANT----"
mkdir fant
cd fant
tar xzvf ../fant.tar.gz
make -f filter_add_noise.make

cd ../


echo "----OPUS----"
tar xzvf opus-1.1.tar.gz
cd opus-1.1
make -f Makefile.unix
    
cd ../


echo "----SOX----"
tar  -xvjf sox-14.4.2.tar.bz2
cd sox-14.4.2/

./configure --enable-static --disable-shared
make
cd ../



tar -xvjf ffmpeg-2.6.9.tar.bz2
tar xzvf lame-3.100.tar.gz

echo "----LAME 3.100----"
cd lame-3.100/

./configure
make
sudo make install
cd ../

pwd
    

echo "----LIBTOOL----"
sudo apt-get install libtool
    

echo "----FFMPEG 2.6.9----"
cd ffmpeg-2.6.9
./configure --enable-gpl --enable-libmp3lame --enable-nonfree --enable-libaacplus --disable-yasm
make
sudo make install
cd ../

echo "----AMR NB----"
unzip ts_126073v030300p0_updated.zip
cd amr-nb

make -f makefile

echo "----AMR WB----"
cd ../ 


unzip T-REC-G.722.2-200811-S\!AnnC\!SOFT-ZST-E_updated.zip
cd G722-2AnxC-v.7.1.0/c-code-v.7.1.0

make -f makefile.gcc


cd ../../

echo "----SPH PIPE----"
tar xzvf sph2pipe_v2.5.tar.gz
cd sph2pipe_v2.5
gcc -o sph2pipe shorten_x.c file_headers.c sph2pipe.c -lm

cd ../ 

echo "----QIO----"
unzip qio_updated.zip
cd aurora-front-end/qio
make

cd ../../


echo "----CODEC 2----"
mkdir -p codec2
cd codec2
unzip ../codec2


mkdir -p build_linux
cd build_linux
cmake ../
make
cd ../../


#echo "----AAC----"
#sudo apt-get --assume-yes install libtool-bin
#tar -xzvf libaacplus-2.0.2.tar.gz
#cd libaacplus-2.0.2
#sudo bash autogen.sh --enable-shared --enable-static

#make
#sudo make install
#cd ../
