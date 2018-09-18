from urllib import request
import ssl

myssl = ssl.create_default_context()
myssl.check_hostname = False
myssl.verify_mode = ssl.CERT_NONE

url = '''
      https://tealprod.tea.state.tx.us/Tea.TxChse.Web/Public/CertificateSearch.aspx
      '''

resp = request.urlopen(url, context=myssl)
