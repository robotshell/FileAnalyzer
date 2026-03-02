import requests, os, tempfile, logging
from .config import MAX_FILE_SIZE, DOWNLOAD_TIMEOUT

def download_file(url, timeout=DOWNLOAD_TIMEOUT, max_size=MAX_FILE_SIZE):
    try:
        r = requests.get(url, timeout=timeout, stream=True)
        if r.status_code != 200:
            logging.warning(f"Failed download {url} (status {r.status_code})")
            return None

        size = int(r.headers.get("Content-Length", 0))
        if size > max_size:
            logging.warning(f"Skipped {url}: file too large ({size} bytes)")
            return None

        suffix = os.path.splitext(url)[1]
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        for chunk in r.iter_content(1024):
            tmp.write(chunk)
        tmp.close()
        return tmp.name

    except Exception as e:
        logging.warning(f"Exception downloading {url}: {e}")
        return None
