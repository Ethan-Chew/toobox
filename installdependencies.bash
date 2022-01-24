
echo Install Dependencies for Toobox
echo Proceeding to Download in 3 Seconds
echo Dependencies installing: chemlib, pillow, matplotlib
echo Else, Ctrl+C to quit
sleep 3

pip3 install chemlib
pip3 install pillow
pip3 install matplotlib

echo Installation Complete!
echo Toobox will launch automatically in 2 Seconds
sleep 2
python3 main.py