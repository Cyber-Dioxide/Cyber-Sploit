# shellcheck disable=SC2028
echo "\n[*] This may take a while \n[+] Installing required packages ..."
sudo apt install python3 > /dev/null
echo "[+] Successfully installed python3"
sudo apt install python3-pip > dev/null
echo "[+] Successfully installed python3-pip"
pip install -r requirements.txt > /dev/null
echo "[+] Successfully installed python3 libraries"
clear
echo "[+] Launching Cyber-Sploit Framework.... /"
sleep 3
python3 Cyber-Framework.py
