from api.searchCert import searchCertificates
import pandas as pd


def generate_csv_data(results):
    # Convert generator object to json
    json = pd.DataFrame(data=results)
            
    # Convert json to csv
    return json.to_csv()
  

def getUnExpiredCert():
        """Gets un expited SHA certificates.

        Returns:
            str: csv of certificates.
        """
        query = "parsed.names: censys.io and tags: trusted"
        fields = ["parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"]
        
        try:
            results = searchCertificates(query, fields)
           
            return generate_csv_data(results)

        except:
            raise Exception(f"While getting the un expired certificates")


certificates = getUnExpiredCert()
print('un expired certificates', certificates)



