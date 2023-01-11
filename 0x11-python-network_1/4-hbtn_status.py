#!usr/bin/python3                                                            
"""fetches https://alx-intranet.hbtn.io/status                               
You must use the package requests"""                                         
                                                                             
if __name__ == "__main__":
    import requests
    r= requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('     - type: ',type(r.text))
    print('     - content: ',r.text)
