from django.conf import settings

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import base64
import rsa

# ---------------------------------------------------------------------------- #
#                                 PATH SAVE KEY                                #
# ---------------------------------------------------------------------------- #
path_save_private_key = str(settings.BASE_DIR)+"/decryptRSA/key/private_key/"
path_save_public_key = str(settings.BASE_DIR)+"/decryptRSA/key/public_key/"

# ---------------------------------------------------------------------------- #
#                   METHOD CREATE PUBLIC_KEY AND PRIVATE_KEY                   #
# ---------------------------------------------------------------------------- #
def generateKey(device_id):
    public_key , private_key = rsa.newkeys(1024)
    
    namePrivateKeyFile = "KEYPRIVATE-"+str(device_id)+'.pem'
    with open(path_save_private_key+namePrivateKeyFile,"wb") as f:
        f.write(private_key.save_pkcs1('PEM'))
        
    namePublicKeyFile = "KEYPUBLIC-"+str(device_id)+'.pem'
    with open(path_save_public_key+namePublicKeyFile,"wb") as f:
        f.write(public_key.save_pkcs1('PEM'))
        
    return {
        'name_private_key' : namePrivateKeyFile,
        'name_public_key' : namePublicKeyFile,
        'public_key' : public_key.save_pkcs1('PEM').decode('utf-8')
    }



# ---------------------------------------------------------------------------- #
#                METHOD DECRYPTION ENCRYPTED DATA TO PRIVATE_KEY               #
# ---------------------------------------------------------------------------- #
def decrypt_tokens(encrypted_data, nameFile):
    
    decode_data = base64.b64decode(encrypted_data)
    
    with open(
        path_save_private_key
        + nameFile.replace("(",'').replace(")",'').replace("," , "").replace("'",""), 
        'rb'
    ) as f:
        private_key = RSA.importKey(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher.decrypt(decode_data)
    
    return decrypted_data.decode()
# ---------------------------------------------------------------------------- #
#                       METHOD GET PUBLIC KEY FOR DEVICE                       #
# ---------------------------------------------------------------------------- #
def getPublicKey(namePublicKeyFile):
    with open(path_save_public_key+namePublicKeyFile,"rb") as f:
        return f.read().decode('utf-8')