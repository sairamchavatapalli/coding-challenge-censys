"""Search certificate data set."""
from censys.search import CensysCertificates

c = CensysCertificates()

def searchCertificates(query, fields):
    """Trigger the censys api.

        Returns:
           List of certificates.
        """
    return c.search(query, fields)
   