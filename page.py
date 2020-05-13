#Copyright Wibucode
import requests, os, sys
from time import sleep
def main():
	os.system("clear")
	print """
   ###
   ###
   ###
   ###
#########
 ####### Author	: WibuCode
  #####	 Github	: https://github.com/wibucode
   ###	 Downloader Page Web
    #
	"""
	web = raw_input("Url web: ")
	namafile = raw_input("Nama file(ex: index.html): ")
	r = requests.get(web)
	req = r.content
	print "\033[92mMendownload page..."
	sleep(1)
	f = open(namafile, "w")
	f.write(req)
	f.close()
	print "\033[96mHasil download ada pada file "+"\033[91m"+namafile
	sleep(1)
	select = raw_input("\033[97mIngin mendownload lagi? y/n: ")
	if select == "y":
		main()
	elif select == "n":
		print "\033[91mKeluar\033[97m"
		sys.exit()
try:
	main()
except KeyboardInterrupt:
	print "Ctrl + C (exit)"
