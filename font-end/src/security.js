import forge from 'node-forge';
function toHex(str) {
  var result = '';
  for (var i=0; i<str.length; i++) {
    result += str.charCodeAt(i).toString(16);
  }
  return result;
}
export const Crypto  = {
    encryptData(public_key,plaintext) {
      // Mã hóa dữ liệu ở đây
      const publicKeyPem = String(public_key.slice(2,-3)).replace(" ","")
      const publicKey = forge.pki.publicKeyFromPem(public_key);
      const ciphertext = publicKey.encrypt(plaintext,'RSA-OAEP');

      // Xử lý kết quả ở đây
      return forge.util.encode64(ciphertext)
    }
}
